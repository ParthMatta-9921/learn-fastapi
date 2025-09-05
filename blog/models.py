from database import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer,String,Text,ForeignKey
#     Use index=True if you often:

# Search by the column (filter(Blog.title == something))

# Sort by it (ORDER BY title)

# Join/filter using it in relationships

# ❌ Don’t bother if:

# The column is rarely used in queries.

# It’s just descriptive (e.g., blog body text, description).

class Blog(Base):
    __tablename__="blogs"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    title:Mapped[str]=mapped_column(String(200),index=True) #length for varchar
    body:Mapped[str]=mapped_column(Text)# long text

    user_id:Mapped[int]=mapped_column(Integer,ForeignKey("users.id"))#creator of the blog


    creator=relationship("User", back_populates="blogs")    


class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    username:Mapped[str]=mapped_column(String(100),index=True)
    email:Mapped[str]=mapped_column(String(100),index=True)
    password:Mapped[str]=mapped_column(String(100))

    blogs=relationship("Blog", back_populates="creator")