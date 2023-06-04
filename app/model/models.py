from typing import List, Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class User(Base):
    '''
    Model representation for `user` table.
    '''

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement="auto")
    email = Column(String, unique=True, index=True)

    accessible_features: Mapped[List["Feature"]] = relationship(
        secondary="feature_access", back_populates="accessed_by"
    )

    # feature_access: Mapped[List["FeatureAccess"]] = relationship(
    #     back_populates="users"
    # )


class Feature(Base):
    '''
    Model representation for `feature` table.
    '''

    __tablename__ = "feature"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement="auto")
    name = Column(String, unique=True, index=True)

    accessed_by: Mapped[List["User"]] = relationship(
        secondary="feature_access", back_populates="accessible_features"
    )

    # feature_access: Mapped[List["FeatureAccess"]] = relationship(
    #     back_populates="features"
    # )


class FeatureAccess(Base):
    '''
    Model representation for  many-to-many relationship between `user` and `feature` tables.
    '''

    __tablename__ = "feature_access"

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    feature_id: Mapped[int] = mapped_column(
        ForeignKey("feature.id"), primary_key=True
    )
    is_enabled = Column(Boolean, default=False)

    # users: Mapped["User"] = relationship(back_populates="feature_access")
    # features: Mapped["Feature"] = relationship(back_populates="feature_access")
