#🧩 Ejercicio 6: Refactorizar procesamiento de ventas (separar lógica/I-O + eficiencia + pruebas)

# Código inicial (mejorable)

def totalize(sales):
    t = 0
    for s in sales:
        if s["status"] == "ok":
            price = s["price"]
            qty = s["qty"]
            disc = 0
            if qty >= 10:
                disc = 0.1
                if s["customer"] == "vip":
                    disc = disc + 0.05
                    subtotal = price * qty
                    subtotal = subtotal - (subtotal * disc)
                    t = t + subtotal
                else:
                    print("bad sale:", s)
                    print("TOTAL:", t)
                    return t

#Problemas típicos
#>• Mezcla lógica con print (difícil de testear)
#• Descuentos “pegados” en el loop
#• No define claramente qué hacer con ventas inválidas
#• Variable disc y t poco descriptivas

#Tu objetivo
#Refactoriza para que:
#• Exista una función pura: calculate_sale_total(sale: dict) -> float (solo calcula)
##• Otra función: calculate_total(sales: list[dict]) -> float (suma)
#• La función que imprime quede aparte (opcional): report_invalid_sales(...)
#• Use nombres claros (total, discount, subtotal)
#• Maneje ventas inválidas sin imprimir en la función de cálculo (por ejemplo: ignorarlas o lanzar excepción, tú defines y lo documentas)

#Pruebas sugeridas
#Crea un conjunto de ventas y verifica:
#• Suma correcta con ventas “ok”
#• Descuento por cantidad ≥ 10 (10%).
#• Descuento extra por customer == "vip" (+5%).
#• Qué pasa con status != "ok" según tu decisión (ignora o error), y prueba ese comportamiento.


BULK_THRESHOLD = 10
BULK_DISCOUNT = 0.10
VIP_DISCOUNT = 0.05


def calculate_discount(sale: dict) -> float:
    discount = 0.0
    if sale["qty"] >= BULK_THRESHOLD:
        discount += BULK_DISCOUNT
    if sale.get("customer") == "vip":
        discount += VIP_DISCOUNT
    return discount


def calculate_sale_total(sale: dict) -> float:
    if sale.get("status") != "ok":
        raise ValueError(f"Venta inválida pasada a calculate_sale_total: {sale}")

    price = sale["price"]
    qty = sale["qty"]
    discount = calculate_discount(sale)
    subtotal = price * qty
    return subtotal * (1 - discount)


def calculate_total(sales: list[dict]) -> float:
    total = 0.0
    for sale in sales:
        if sale.get("status") == "ok":
            total += calculate_sale_total(sale)
    return total


def report_invalid_sales(sales: list[dict]) -> None:
    invalid = [s for s in sales if s.get("status") != "ok"]
    for sale in invalid:
        print("Venta inválida:", sale)
        
        



import pytest
from sales import calculate_sale_total, calculate_total, report_invalid_sales




@pytest.fixture
def venta_normal():
    return {"status": "ok", "price": 100.0, "qty": 1, "customer": "regular"}

@pytest.fixture
def venta_bulk():
    return {"status": "ok", "price": 50.0, "qty": 10, "customer": "regular"}

@pytest.fixture
def venta_vip():
    return {"status": "ok", "price": 200.0, "qty": 1, "customer": "vip"}

@pytest.fixture
def venta_bulk_vip():
    return {"status": "ok", "price": 100.0, "qty": 10, "customer": "vip"}

@pytest.fixture
def venta_invalida():
    return {"status": "error", "price": 50.0, "qty": 2, "customer": "regular"}




class TestCalculateSaleTotal:

    def test_venta_sin_descuento(self, venta_normal):
        # 100 * 1 * (1 - 0.0) = 100.0
        assert calculate_sale_total(venta_normal) == 100.0

    def test_descuento_bulk(self, venta_bulk):
        # 50 * 10 = 500; descuento 10% → 450.0
        assert calculate_sale_total(venta_bulk) == 450.0

    def test_descuento_vip(self, venta_vip):
        # 200 * 1 = 200; descuento 5% → 190.0
        assert calculate_sale_total(venta_vip) == 190.0

    def test_descuento_bulk_y_vip(self, venta_bulk_vip):
        # 100 * 10 = 1000; descuento 15% → 850.0
        assert calculate_sale_total(venta_bulk_vip) == 850.0

    def test_venta_invalida_lanza_error(self, venta_invalida):
        # Decisión: lanza ValueError si status != 'ok'
        with pytest.raises(ValueError, match="inválida"):
            calculate_sale_total(venta_invalida)




class TestCalculateTotal:

    def test_suma_ventas_ok(self, venta_normal, venta_bulk):
        # 100.0 + 450.0 = 550.0
        ventas = [venta_normal, venta_bulk]
        assert calculate_total(ventas) == 550.0

    def test_ignora_ventas_invalidas(self, venta_normal, venta_invalida):
        # Solo cuenta venta_normal = 100.0
        ventas = [venta_normal, venta_invalida]
        assert calculate_total(ventas) == 100.0

    def test_lista_vacia(self):
        assert calculate_total([]) == 0.0

    def test_todas_invalidas(self, venta_invalida):
        assert calculate_total([venta_invalida, venta_invalida]) == 0.0



class TestReportInvalidSales:

    def test_imprime_ventas_invalidas(self, venta_invalida, capsys):
        report_invalid_sales([venta_invalida])
        captured = capsys.readouterr()
        assert "Venta inválida" in captured.out

    def test_no_imprime_ventas_ok(self, venta_normal, capsys):
        report_invalid_sales([venta_normal])
        captured = capsys.readouterr()
        assert captured.out == ""