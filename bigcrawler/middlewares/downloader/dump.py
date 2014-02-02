class HTMLDumper(object):
    def process_response(self, request, response, spider):
        print response.status, " ", response.url
        return response
