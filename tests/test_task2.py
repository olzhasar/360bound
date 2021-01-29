import pytest
from task2 import Printer, Canon, HP, Order


class TestPrinter:
    @pytest.mark.parametrize(
        "model, obj, print_result",
        [
            ["Canon EL727", Canon, "Canon"],
            ["HP MFP127", HP, "HP"],
        ],
    )
    def test_get_by_model_ok(self, model, obj, print_result):
        instance = Printer.get_by_model(model)

        assert isinstance(instance, obj)
        assert isinstance(instance, Printer)
        assert instance.print() == print_result

    def test_get_by_model_non_existing(self):
        with pytest.raises(RuntimeError):
            Printer.get_by_model("Wrong model")


@pytest.mark.parametrize(
    "printer_model, expected",
    [
        ["Canon EL727", "Canon"],
        ["HP MFP127", "HP"],
    ],
)
def test_order_print(printer_model, expected):
    order = Order("TEST CONTENT", printer_model)

    assert order.print() == expected
