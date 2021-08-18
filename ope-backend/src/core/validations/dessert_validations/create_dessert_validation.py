def create_dessert_validation(name: str, description: str, price: float, amount: int, img: str):
    message: list[str] = []
    if not isinstance(name, str) or name is None or len(name) > 40 or name == "":
        message.append("Nome inválido")
    if not isinstance(description,str) or description is None or len(description) > 200 or description == "":
        message.append("Descrição inválida")
    if not isinstance(price, float) or price is None:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None:
        message.append("Quantidade inválida")
    if not isinstance(img, str) or img is None:
        message.append("Imagem obrigatória")
    return message