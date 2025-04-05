from schema.message import MesageResp, MessageSend, MessageRefactor



def get_all_messages() -> list[MesageResp]:
    pass


def get_messages_by_user(user_id: int) -> list[MesageResp]:
    pass


def get_message_by_id(message_id: int) -> MesageResp:
    pass


def send_message(body: MessageSend) -> MesageResp:
    pass


def delete_message(message_id: str) -> MesageResp:
    pass

def refactor_message(message_id: str, body: MessageRefactor) -> MesageResp:
    pass

