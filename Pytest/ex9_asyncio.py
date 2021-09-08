

async def call_to_my_async_function():
    return 'banana'

import pytest

@pytest.mark.asyncio
async def test_an_async_function():
    result = await call_to_my_async_function()
    assert result == 'banana'