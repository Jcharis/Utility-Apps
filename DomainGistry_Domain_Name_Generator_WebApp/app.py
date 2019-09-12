from flask import Flask,render_template,request
new_domain = ['app',
'site',
'online',
'xyz',
'tech',
'shop',
'blog',
'space',
'live',
'life',
'website',
'news',
'ninja',
'solutions',
'expert',
'services',
'media',
'rocks',
'company',
'guru',
'club',
'today',
'agency',
'technology',
'tips',
'center',
'link',
'click',
'ltd',
'win',
'work']

common_domain = [
'com',
'edu',
'net',
'org',
'site',
'co',
'io',
'ai',
'app',
'ca',
'uk',
'ua',
'us',
'ru',
'ch']

extra_domain =[
"asia",
"africa",
"us",
"me",
"biz",
"info",
"name",
"mobi",
"cc",
"tv",
"ly",
"it",
"to",
"eu",
"ch",
"online"]


prefix_domain = [
'a',
'i',
'e',
'the',
'my',
'me',
'we',
'top',
'best',
'get',
'co',
'nu',
'up',
'new',
'live',
'bestof',
'meta',
'just',
'99',
'101',
'insta',
'try',
'hit',
'go',
're',
'dr',
'mr',
'bit',
'net',
'hot',
'beta',
'you',
'our',
'x',
'buy',
'for',
'pro',
'ez',
'on',
'v',
'hd',
'max',
'digi',
'free',
'very',
'all',
'easy',
'cool',
'air',
'next',
'find',
'uber',
]

suffix_domain = [
"online.com",
"world.com",
"io.com",
"me.com",
"you.com",
"up.com",
"new.com",
"blog.com",
"web.com",
"hd.com",
"hq.com",
"tip.com",
"tips.com",
"guru.com",
"link.com",
"sumo.com",
"mob.com",
"lab.com",
"labs.com",
"list.com",
"info.com",
"jar.com",
"egg.com",
"site.com",
"app.com",
"apps.com",
"net.com",
"inc.com",
"247.com",
"360.com",
"24x7.com",
"corp.com",
"page.com",
"llc.com",
"now.com",
"all.com",
"box.com",
"base.com",
"zone.com",
"zoom.com",
"bit.com",
"bits.com",
"byte.com",
"bros.com",
"cart.com",
"sale.com",
"shop.com",
"store.com",
"free.com",
"soft.com",
"101.com",
"center.com",
"pro.com",
"pros.com",
"co.com",
"space.com",
"hub.com",
"spot.com",
"ware.com",
"talk.com",
"place.com",
"kit.com",
"pad.com",
"tool.com",
"bot.com",
"bots.com",
"bee.com",
"doc.com",
".com",
"al.com",
"ity.com",
"iput.com",
"ally.com",
"ality.com",
"alness.com",
"ipital.com"]

# Initialize App
app = Flask(__name__)

def shufflize(word):
	new_word = word.split(" ")
	if len(new_word) == 2:
		first_text = new_word[0]
		last_text = new_word[1]
		result = "{}{}".format(last_text,first_text)
	elif len(new_word) == 3:
		first_text = new_word[0]
		mid_text = new_word[1]
		last_text = new_word[2]
		result = "{}{}{}".format(last_text,first_text,mid_text)
	else:
		result = "".join(new_word)
	return result


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/generate',methods=['POST','GET'])
def generate():
	if request.method == 'POST':
		old_text = request.form['raw_text']
		raw_text = "".join(old_text.lower().split(" "))
		shuffled_text = shufflize(old_text.lower())
		word_tokens = len(old_text.split(" "))
		char_len = len(raw_text)
		word_stats = 'Tokens:{},\nCharacters:{}'.format(word_tokens,char_len)
		cust_list_new = ['{}.{}'.format(raw_text,i) for i in new_domain ]
		cust_list_common = ['{}.{}'.format(raw_text,i) for i in common_domain ]
		cust_list_extra = ['{}.{}'.format(raw_text,i) for i in extra_domain ]
		cust_list_prefix = ['{}{}.com'.format(i,raw_text) for i in prefix_domain ]
		cust_list_suffix = ['{}{}'.format(raw_text,i) for i in suffix_domain ]
		cust_list_shuffled = ['{}.{}'.format(shuffled_text,i) for i in common_domain ]

	return render_template('index.html',raw_text=raw_text,old_text=old_text,
		cust_list_new = cust_list_new,
		cust_list_suffix=cust_list_suffix,
		cust_list_prefix=cust_list_prefix,
		cust_list_extra=cust_list_extra,
		cust_list_common=cust_list_common,
		cust_list_shuffled=cust_list_shuffled,
		word_stats=word_stats)


if __name__ == '__main__':
	app.run(debug=True)