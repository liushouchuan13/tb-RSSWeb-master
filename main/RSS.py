import feedparser

class RSS:
    def __init__(self, link):
        self.link = link
        self.ok = False

        self._update()

    def _update(self):
        """ 查看更新 """

        self.feed = feedparser.parse(self.link)
        if self.feed.get("feed").get("title"):
            self.title = self.feed['feed']['title']
            self.updated = self.feed['feed']['updated_parsed']
            self.ok = True


    def articles(self):
        """ 文章列表 """
        return self.feed['entries']

    def __len__(self):
        return len(self.feed['entries'])


if __name__ == '__main__':
    link = "http://www.read.org.cn/feed"
    zhihu = RSS(link)

    print(zhihu)