import itertools
from pprint import pprint


class Action:
    """
    This is the Action class.
    """

    def __init__(self, object_, transaction, type_):
        self.object_ = object_
        self.transaction = transaction
        assert type_ in ("WRITE", "COMMIT", "ROLLBACK",
                         "LOCK", "UNLOCK", "WAIT")
        self.type_ = type_

    def __str__(self):
        return f"Action('{self.object_}', '{self.transaction}', '{self.type_}')"
    __repr__ = __str__

    def __eq__(self, other):
        return ((self.object_ == other.object_) and
                (self.transaction == other.transaction) and
                (self.type_ == other.type_))


class Transaction:
    def __init__(self, actions, timestamp):
        self.actions = actions
        self.timestamp = timestamp
        self.actions_index = 0

    def __repr__(self):
        return f"Transaction({self.actions}, {self.timestamp}, {self.actions_index})"


def release_locks(locks, transaction_name):
    actions_taken = []
    # Unlock all locks
    locks_held = set()
    for object_, holding_transaction_name in locks.items():
        if holding_transaction_name == transaction_name:
            locks_held.add(object_)
    for object_ in sorted(locks_held):

        del locks[object_]
        action = Action(object_, transaction_name, "UNLOCK")
        actions_taken.append(action)
        print(f"  Doing UNLOCK {action}")

    return actions_taken


def do_one_action_per_transaction(transactions, locks):
    print("\nDoing one action for each transaction:")
    actions_taken = []
    for transaction_name in sorted(transactions.keys()):
        print(f" Trying to do {transaction_name}")
        transaction = transactions[transaction_name]
        if transaction.actions_index < len(transaction.actions):
            action = transaction.actions[transaction.actions_index]
            if action.type_ == "COMMIT":
                # Do commit
                print(f"  Doing COMMIT {action}")
                actions_taken.append(action)

                actions_taken.extend(release_locks(locks, transaction_name))

                # Increment action index
                transaction.actions_index += 1

                continue

            if action.type_ == "WRITE":
                if (action.object_ not in locks) or (locks[action.object_] == transaction_name):
                    if action.object_ not in locks:
                        # Get Lock
                        locks[action.object_] = transaction_name
                        locking_action = Action(
                            action.object_, transaction_name, "LOCK")
                        actions_taken.append(locking_action)
                        print(f"  Doing LOCK {locking_action}")
                    # Do action
                    print(f"  Doing WRITE {action}")
                    actions_taken.append(action)

                    # Increment action index
                    transaction.actions_index += 1

                    continue
                name_of_transaction_holding_lock = locks[action.object_]
                transaction_holding_lock = transactions[name_of_transaction_holding_lock]
                if transaction_holding_lock.timestamp < transaction.timestamp:  # this trans is lower priority
                    print(f"  Doing ROLLBACK ({transaction} is younger)")
                    actions_taken.append(
                        Action("NA", transaction_name, "ROLLBACK"))
                    actions_taken.extend(
                        release_locks(locks, transaction_name))
                    transaction.actions_index = 0
                    continue
                else:  # this trans is higher priority

                    # WAIT
                    print(f"  Doing WAIT ({transaction} is older)")
                    actions_taken.append(
                        Action("NA", transaction_name, "WAIT"))
    return actions_taken


def wait_die_scheduler(actions):
    transactions = {}  # transaction name -> Transaction object
    locks = {}  # object -> transaction name
    actions_taken = []

    for action, current_time in zip(actions, itertools.count()):

        # For each transaction, ordered by name, try to do action
        actions_taken.extend(
            do_one_action_per_transaction(transactions, locks))

        # Add action to appropriate transaction
        print(f"\nAdding {action} to its transaction")
        if action.transaction in transactions:
            current_transaction = transactions[action.transaction]
        else:
            # Transaction is new create it
            current_transaction = Transaction([], current_time)
            transactions[action.transaction] = current_transaction
        current_transaction.actions.append(action)

    while True:
        previous_length = len(actions_taken)
        actions_taken.extend(
            do_one_action_per_transaction(transactions, locks))
        if previous_length == len(actions_taken):
            break

    return actions_taken


def test2():
    actions = [
        Action(object_="A", transaction="pear", type_="WRITE"),
        Action(object_="B", transaction="apple", type_="WRITE"),
        Action(object_="B", transaction="pear", type_="WRITE"),
        Action(object_="A", transaction="apple", type_="WRITE"),
        Action(object_="NA", transaction="apple", type_="COMMIT"),
        Action(object_="NA", transaction="pear", type_="COMMIT"),
    ]
    expected = [Action('A', 'pear', 'LOCK'),
                Action('A', 'pear', 'WRITE'),
                Action('B', 'apple', 'LOCK'),
                Action('B', 'apple', 'WRITE'),
                Action('NA', 'pear', 'WAIT'),
                Action('NA', 'apple', 'ROLLBACK'),
                Action('B', 'apple', 'UNLOCK'),
                Action('B', 'pear', 'LOCK'),
                Action('B', 'pear', 'WRITE'),
                Action('NA', 'apple', 'ROLLBACK'),
                Action('NA', 'apple', 'ROLLBACK'),
                Action('NA', 'pear', 'COMMIT'),
                Action('A', 'pear', 'UNLOCK'),
                Action('B', 'pear', 'UNLOCK'),
                Action('B', 'apple', 'LOCK'),
                Action('B', 'apple', 'WRITE'),
                Action('A', 'apple', 'LOCK'),
                Action('A', 'apple', 'WRITE'),
                Action('NA', 'apple', 'COMMIT'),
                Action('A', 'apple', 'UNLOCK'),
                Action('B', 'apple', 'UNLOCK')]
    print("Actions = ")
    pprint(actions)
    print("Expected = ")
    pprint(expected)
    result = wait_die_scheduler(actions)
    print("Result = ")
    pprint(result)
    assert expected == result


test2()
