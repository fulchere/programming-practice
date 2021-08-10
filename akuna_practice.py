# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.

class MarkingPositionMonitor:
    def __init__(self):
        self.num = 0

    def on_event(self, message):
        if message['type'] == "NEW":
            if message['side'] == "SELL":
                self.num -= message['quantity']
            return self.num
        elif message['type'] == "ORDER_ACK":
            print("type is new")
        elif message['type'] == "ORDER_REJECT":
            print("type is new")
        elif message['type'] == "CANCEL":
            print("type is new")
        elif message['type'] == "CANCEL_ACK":
            print("type is new")
        elif message['type'] == "CANCEL_REJECT":
            print("type is new")
        elif message['type'] == "FILL":
            print("type is new")
        else:
            return self.num


mon = MarkingPositionMonitor()
print(mon.on_event({"type": "NEW", "symbol": "IMIMP", "order_id": 1,
                    "side": "SELL", "quantity": 800, "time": "2017-03-15T10:15:10.975187"}))
