"""
Pydantic models for VLLM configuration, used primarily for RL training with TRL + grpo
"""

from pydantic import BaseModel, Field


class VllmConfig(BaseModel):
    """
    Configuration for VLLM server
    """

    device: str | None = Field(
        default="auto",
        json_schema_extra={"description": "Device to use for VLLM"},
    )
    tensor_parallel_size: int | None = Field(
        default=None,
        json_schema_extra={"description": "Tensor parallel size for VLLM"},
    )
    data_parallel_size: int | None = Field(
        default=None,
        json_schema_extra={"description": "Data parallel size for VLLM"},
    )
    gpu_memory_utilization: float | None = Field(
        default=0.9,
        json_schema_extra={"description": "GPU memory utilization for VLLM"},
    )
    dtype: str | None = Field(
        default="auto",
        json_schema_extra={"description": "Data type for VLLM"},
    )
    max_model_len: int | None = Field(
        default=None,
        json_schema_extra={
            "description": "Maximum length of the model context for VLLM"
        },
    )
    enable_prefix_caching: bool | None = Field(
        default=None,
        json_schema_extra={"description": "Enable prefix caching for VLLM"},
    )
    host: str | None = Field(
        default="0.0.0.0",  # nosec B104
        json_schema_extra={"description": "Host for the vLLM server to start on"},
    )
    port: int | None = Field(
        default=8000,
        json_schema_extra={"description": "Port of the vLLM server to start on"},
    )

    enable_reasoning: bool | None = Field(
        default=None,
        json_schema_extra={"description": "Enable reasoning for VLLM"},
    )
    reasoning_parser: str | None = Field(
        default=None,
        json_schema_extra={"description": "Reasoning parser for VLLM"},
    )
