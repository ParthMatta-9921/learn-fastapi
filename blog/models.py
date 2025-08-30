from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,String,Text



class Blog(Base):
    __tablename__="blogs"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    title:Mapped[str]=mapped_column(String(200),index=True) #length for varchar
    body:Mapped[str]=mapped_column(Text)# long text

#     Use index=True if you often:

# Search by the column (filter(Blog.title == something))

# Sort by it (ORDER BY title)

# Join/filter using it in relationships

# ❌ Don’t bother if:

# The column is rarely used in queries.

# It’s just descriptive (e.g., blog body text, description).