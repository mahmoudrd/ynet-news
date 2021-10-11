
import requests
import lxml.html
import logging
import sys


URL = "http://www.ynet.co.il/Integration/StoryRss2.xml"



def get_ynet(url=URL):
	res = requests.get(url)
	if res.status_code != 200:
		sys.exit('\x1b[31m' + "Page not found" + '\x1b[0m')
	doc = lxml.etree.fromstring(res.content)
	cells = doc.xpath("//item")
	return news


def table(news):
	title = decription = link  = ""
	list_html = index_html = ""
	_LIST_HTML = \
		'''
		<tr>
			<td style="border:1px solid green;">{title}</td>
			<td style="border:1px solid green;">{description}</td>
			<td style="border:1px solid green;">{link}</td>
		</tr>
		'''
	_INDEX_HTML = \
		'''
		<html>
			<head>
				<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
				<meta content="utf-8" http-equiv="encoding">
				<center>
					<h1><FONT COLOR="#FF0000">Breaking news<h1>
				</center>
			</head>
			<body>
				<table style="border:1px solid red;border-collapse:collapse;">
					<tr>
					<th style="border:1px solid green;">title</th>
					<th style="border:1px solid green;">description</th>
					<th style="border:1px solid green;">link</th>
					</tr>
					{list}
				</table>
			</body>
		</html>
		'''
	lists = []
	for cell in news:
		title = cell.xpath(".//title/text()")[0]
		description = cell.xpath("./description/text()")[0]
		link = cell.xpath("./link/text()")[0]
		link = f'<a href="url">{link}</a>'
		list_html = _LIST_HTML.format(
			title=title,
			description=description,
			link=link,
		)
		lists.append(list_html)
	index_html = _INDEX_HTML.format(list='\n'.join(lists))
	return index_html



def run():
	news = get_ynet()
	html_table = table(news)
	with open('index.html', 'w+') as writer:
		writer.write(html_table)


if __name__ == '__main__':
	run()
