import pytest
from src.bus import MicroserviceEventBus, WebhookEvent

def test_publish_subscribe_flow():
    bus = MicroserviceEventBus()
    dispatched_items = []

    bus.subscribe("order.placed", lambda e: dispatched_items.append(e.payload["order_id"]))
    
    evt = WebhookEvent(topic="order.placed", payload={"order_id": "ord-889"})
    count = bus.publish(evt)

    assert count == 1
    assert len(dispatched_items) == 1
    assert dispatched_items[0] == "ord-889"
    assert len(bus.get_history("order.placed")) == 1

def test_empty_topic_rejected():
    bus = MicroserviceEventBus()
    with pytest.raises(ValueError, match="cannot be empty"):
        bus.subscribe("", lambda e: None)
