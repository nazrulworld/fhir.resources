# _*_ coding: utf-8 _*_

from typing import List, Optional

from pydantic import BaseModel, Field

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"


class ExpressionNode(BaseModel):
    """ """

    node_type: str = Field(..., title="Node Type")
    text: str = Field(None, title="Text")
    terminal_node_text: Optional[List[str]] = Field(None, title="Terminal Node Text")
    children: Optional[List["ExpressionNode"]] = Field(None, title="Children node")


# important
ExpressionNode.update_forward_refs()
