import feedparser

feed = feedparser.parse("http://all-rss.ru/feed-109-novosti-universiteta-itmo/")
# всё парсится ок

feed_entries = feed.entries

for entry in feed.entries:

    title = entry.title
    link = entry.link
    summary = entry.summary
    desc = entry.description
    author = entry.author
    pubDate = entry.published

    print('title: {}\nlink: {}\nsummary: {}\nauthor: {}\ndate: {}\n'.format(title, link, summary, author, pubDate))
