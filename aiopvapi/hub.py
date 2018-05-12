"""Hub class acting as the base for the PowerView API."""

from aiopvapi.helpers.api_base import ApiBase
from aiopvapi.helpers.tools import join_path
from aiopvapi.helpers.constants import ATTR_USER_DATA, \
    ATTR_HUB_NAME, ATTR_HUB_NAME_UNICODE
from aiopvapi.helpers.tools import base64_to_unicode

class Hub(ApiBase):
    api_path = 'api'

    def __init__(self, request):
        super().__init__(request, self.api_path)

    async def get_userdata(self):
        userdata_path = join_path(self._base_path, 'userdata')
        userdata = await self.request.get(userdata_path)
        if ATTR_USER_DATA in userdata:
            userdata = userdata[ATTR_USER_DATA]
        if ATTR_HUB_NAME in userdata:
            userdata[ATTR_HUB_NAME_UNICODE] = \
                base64_to_unicode(userdata[ATTR_HUB_NAME])
        return userdata

