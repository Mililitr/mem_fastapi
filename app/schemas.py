from pydantic import BaseModel, ConfigDict

class MemeBase(BaseModel):
    text: str
    image_url: str

class MemeCreate(MemeBase):
    pass

class MemeUpdate(MemeBase):
    pass

class Meme(MemeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)