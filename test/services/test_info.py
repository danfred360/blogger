import pytest

from src.config import get_config
from src.services.info.info_service import InfoService


@pytest.mark.asyncio
async def test_search_google():
    info = InfoService(get_config())
    query = "open source software"
    num_results = 5

    results = await info.search_google(query, num_results)

    assert len(results) == num_results
