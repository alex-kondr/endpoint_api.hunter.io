from pydantic import BaseModel


class PersonModel(BaseModel):
    domain: str = "gmail.com"
    first_name: str = "Foo"
    last_name: str = "Bar"


class EmailVerify(BaseModel):
    status: str = "Not found"


class Email(BaseModel):
    email: str = "email@gmail.com"