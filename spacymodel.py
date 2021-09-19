import spacy
import re
import datefinder
import datetime
from spacy.matcher import PhraseMatcher
import datetime
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

nlp=spacy.load('en_core_web_sm')

def find_food(email):

	matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

	#terms_list = ['ice cream', 'cookies', 'pork', 'beef', 'chicken', 'cola', 'lemonade', 'gumball', 'kettle', 'pecans', 'walnuts', 'marshmallow', 'oatmeal', 'lentils', 'cheese', 'hummus', 'quinoa', 'marshmallows', 'shrimp', 'prosciutto', 'milk', 'pepperroni', 'coleslaw', 'ajweh', 'cupcakes', 'conchas', 'bagels', 'lemons', 'asparagus', 'pretzels', 'buns', 'eggnog', 'tamari', 'marinade', 'mayonnaise', 'icing', 'dates', 'truffles', 'besan', 'mustard', 'carrots', 'turkey', 'biscuits', 'apples', 'wafers', 'creamer', 'pumpkin', 'peas', 'beans', 'liverwurst', 'mole', 'rice', 'penne', 'linguine', 'pappardelle', 'margarita', 'elbows', 'rotini', 'fettuccine', 'cereal', 'mandarins', 'brownies', 'divinity', 'spirals', 'egg', 'almonds', 'mortadella', 'blackberries', 'cherry', 'soda', 'chocolate', 'cornstarch', 'sprinkles', 'popcorn', 'capers', 'salad', 'semolina', 'ginger', 'limeade', 'guacamole', 'kielbasa', 'giardiniera', 'oatmilk', 'cheesecake', 'salsa', 'water', 'bratwurst', 'salmon', 'cod', 'bars', 'croissants', 'cucumbers', 'moussaka', 'caribbean', 'strawberry', 'edamame', 'farro', 'cauliflower', 'marinara', 'pimientos', 'yuca', 'marzipan', 'avocados', 'corn', 'pineapple', 'grapefruit', 'raspberries', 'pandoro', 'caramel', 'cranberries', 'sazon', 'midgees', 'babaganoush', 'sazonador', 'emoliente', 'chorizos', 'apricots', 'papad', 'catsup', 'molasses', 'jellies', 'triticale', 'buckwheat', 'poi', 'zwieback', 'lard', 'wasabi', 'miso', 'natto', 'okara', 'tempeh', 'kale', 'whiting', 'ballyhoo', 'sorbet', 'gelato', 'conchiglie', 'spaghetti', 'rotelli', 'lasagna', 'talancina', 'soup', 'broth', 'teriyaki', 'pudding', 'pierogies', 'mozzarella', 'sweetener', 'sorbetto', 'puffers', 'croutons', 'muffins', 'pistachios', 'sauce', 'patties', 'cadbury', 'bacon', 'burritos', 'spread', 'applesauce', 'shortening', 'jelly', 'tortillas', 'sherbet', 'donouts', 'ditalini', 'cashews', 'bread', 'meatball', 'peaches', 'bar', 'salametti', 'bluberries', 'rigatoni', 'fusilli', 'anchovies', 'syrup', 'mackerel', 'piccante', 'estrellitas', 'galletitas', 'sandwiches', 'scrapple', 'arugula', 'dressing', 'pancakes', 'longaniza', 'burrito', 'marmalade', 'paste', 'gari', 'flour', 'conscons', 'aiali', 'desserts', 'granola', 'garbanzos', 'applesuace', 'pie', 'saltines', 'waffles', 'matzos', '479', 'fusillo', 'creamy', 'teff', 'wraps', 'carmarsh', 'manicotti', 'crackerz', 'beets', 'menudo', 'ravioli', 'jos', 'delishaved', 'braunschweiger', 'pipian', 'relish', 'tastykrisps', 'peanuts', 'pears', 'banana', 'meatballs', 'yogurt', 'chips', 'cacao', 'macaroons', 'brioche', 'dip', 'yoghurt', 'alcaparrado', 'snakaroons', 'chai', 'vinaigrette', 'peanut', 'passata', 'fettuccini', 'naan', 'pickles', 'chimichangas', 'chimichanga', 'tostadas', 'gelatin', 'puttanesca', 'pops', 'tea', 'bbq', 'horchata', 'spelt', 'tart', 'flatbreads', 'gels', 'stroopwafels', 'pizza', 'limburger', 'oats', 'cappuccino', 'sausage', 'macaroon', 'enchilada', 'preserves', 'sofrito', 'margarine', 'panela', 'cakes', 'boysenberries', 'tortiglioni', 'spaetzle', 'recaito', 'vermicelli', 'huitlacoche', 'maraschinos', 'pasta', 'tamarind', 'seasoning', 'tilapia', 'decaf', 'stevia', 'puffins', 'jam', 'cassava', 'sourcream', 'noodles', 'singles', 'honeycrisp', 'frosting', 'chanterelles', 'lemonaise', 'mayo', 'rotelle', 'grahams', 'baguette', 'bites', 'kimchee', 'brownie', 'chili', 'licorice', 'caramels', 'bisque', 'cocoa', 'vegetables', 'tamales', 'consomme', 'sardines', 'burgers', 'oatsnack', 'kraut', 'candies', 'lollipops', 'spaghettini', 'hermits', 'breadsticks', 'gumdrops', 'cavatelli', 'pennoni', 'peppardelle', 'squeeze', 'sriracha', 'krimpies', 'crisps', 'mushrooms', 'creole', 'guacachip', 'calamari', 'franks', 'flaxseed', 'mango', 'sundae', 'arrabiatta', 'hamburger', 'potatoes', 'parfait', 'tortelloni', 'tortellini', 'okra', 'moussecake', 'sugar', 'swirl', 'basil', 'assorted', 'grape', 'muenster', 'mocha', 'soynuts', 'hommus', 'tahineh', 'cheddar', 'raisin', 'rolls', 'pizzas', 'mousse', 'barbecue', 'poppers', 'rosemary', 'camembert', 'peperoncini', 'eucalipto', 'gingerbread', 'tomatoes', 'mustards', 'tzatziki', 'hummous', 'turmeric', 'parsley', 'sage', 'savory', 'saucerkraut', 'rub', 'hominy', 'chocolatey', 'mints', 'maraschino', 'cereals', 'syrups', 'crispbread', 'lychees', 'sushi', 'tuna', 'risotto', 'pozole', 'bouillon', 'biscuit', 'gravy', 'aioli', 'fruity', 'tapioca', 'chipotle', 'caldereta', 'dijonnaise', 'straws', 'curd', 'muesli', 'squid', 'panko', 'menudito', 'wakame', 'kombu', 'meringues', 'preserve', 'breadcrumbs', 'socorro', 'seitan', 'tofu', 'hatch', 'bruschetta', 'reddiegg', 'lingonberries', 'mix', 'halva', 'katchup', 'dolmas', 'squares', 'milkshakes', 'muffin', 'smartcarb', 'curry', 'xylitol', 'asadero', 'paneer', 'pepper', 'chickpea', 'myzithra', 'ghee', 'strozzapreti', 'toastables', 'tapenade', 'steakburgers', 'saucekraut', 'casarecce', 'vegenaise', 'fukujinzuke', 'chorizo', 'squasch', 'maltose', 'pruuns', 'yams', 'saueruben', 'wieners', 'snacks', 'rakkyo', 'cheesesticks', 'scones', 'tiramisu', 'donuts', 'cracklebred', 'chocorooms', 'cilantro', 'oregano', 'tarragon', 'kabobs', 'puffcorn', 'cheeseburger', 'mostaccioli', 'gnocchi', 'pesto', 'orca', 'chia', 'prunes', 'flapjack', 'caesar', 'paleochef', 'halvah', 'casero', 'palmeritas', 'shells', 'salsagheti', 'meatloaf', 'pastries', 'treat', 'cupkakes', 'paella', 'bananas', 'cashewmilk', 'burger', 'sopressata', 'taquitos', 'mangos', 'coconutmilk', 'twists', 'liquorice', 'lemon', 'scallops', 'stromboli', 'juice', 'danish', 'cupcake', 'strudel', 'jambalaya', 'colby', 'rugalah', 'raspberry', 'dumplings', 'treats', 'sandwich', 'drink', 'almondmilk', 'soymilk', 'nectarines', 'hibiscus', 'bananamilk', 'kombucha', 'chamoy', 'flaxmilk', 'cornichons', 'creamsoda', 'vinegar', 'beverage', 'fettucine', 'quiche', 'surcralose', 'falafel', 'freshmints', 'seltzer', 'cookie', 'nectar', 'minis', 'minipops', 'duritos', 'ringpop', 'cocktail', 'rings', 'punch', 'rellenitas', 'roll', 'snickerdoodles', 'runts', 'dum', 'spangler', 'chill', 'sarsaparilla', 'bark', 'chocolates', 'trufle', 'peach', 'pistachio', 'chewy', 'ponche', 'pretzel', 'bubblegum', '180', 'stirrers', 'frutesca', 'limonada', 'chocolatier', 'wafer', 'gummy', 'mangazo', 'smoothie', 'lollipos', 'clusters', 'shortbread', 'confections', 'nuts', 'bueno', 'coffee', 'giardinera', 'puffs', 'peppermint', 'fudge', 'coffeebar', 'favas', 'orangeade', 'pomegranate', 'beer', 'toffee', 'barazek', 'chestnut', 'funkmeister', 'ricotta', 'tacos', 'cornbread', 'cake', 'cubes', 'ciliegine', 'eggs', 'cherries', 'pita', 'bundt', 'loaf', 'donut', 'tahini', 'focaccia', 'gouda', 'ciabatta', 'panettone', 'quesadilla', 'cakebabies', 'parmesan', 'cracker', 'bandito', 'celery', 'cinnamon', 'grits', 'veggie', 'peppertrio', 'chunks', 'jasminerice', 'kolkas', 'peppers', 'eggplant', 'kalettes', 'huckleberry', 'peppercorns', 'cayenne', 'fillets', 'spices', 'crawfish', 'oranges', 'fondant', 'toastable', 'blondies', 'sourdough', 'snack', 'havarti', 'frichik', 'mocktails', 'cranberry', 'sfogliette', 'apple', 'frankfurter', 'pollock', 'blackberry', 'mussels', 'finocchiona', 'pescato', 'pierogi', 'buttermilk', 'fiori', 'fioretti', 'ferruccine', 'empanadas', 'olives', 'baklava', 'kringle', 'kringles', 'paccheri', 'orzo', 'funwich', 'confection', 'cavatappi', 'pies', 'chutney', 'udon', 'agnolotti', 'beefjerky', 'blintzes', 'falafet', 'taffy', 'smooth', 'croissant', 'tarts', 'ravioloni', 'dillapeno', 'pickle', 'crepes', 'hilopitaki', 'chutneys', 'palmier', 'cider', 'lassi', 'andouille', 'sopes', 'panino', 'tortilla', 'chimmichurri', 'caponata', 'succotash', 'corndogs', 'mushroom', 'artichoke', 'hushpuppies', 'marinated', 'topping', 'barbacoa', 'base', 'quesadillas', 'sucralose', 'crustoli', 'hoagie', 'crostini', 'bruschette', 'kefir', 'arancini', 'pineapples', 'bulgur', 'tarama', 'spanakopita', 'srirachanaise', 'sorullos', 'glaze', 'pulao', 'gumbo', 'empanada', 'banger', 'tequenos', 'potstickers', 'jackfruit', 'giardeniera', 'jalapeno', 'artichokes', 'knockwurst', 'nopalitos', 'pizzetta', 'chickpeas', 'casserole', 'taboule', 'polenta', 'kasekariner', 'kalekopita', 'wings', 'flan', 'curtido', 'cobbler', 'spatzle', 'tagliatelle', 'macaroni', 'fettuce', 'ranch', 'razz', 'chimichurri', 'fondue', 'fig', 'weisswurst', 'knackwurst', 'pizzeti', 'worcestershire', 'colacion', 'smoothies', 'blondie', 'shortcake', 'decorating', 'burrata', 'mantecadas', 'mugging', 'scone', 'chews', 'bagel', 'crescents', 'flounder', 'kiwi', 'cakepops', 'stuffing', 'chococherries', 'shanklish', 'catfish', 'gum', 'latte', 'pandeyucas', 'sfornatini', 'madalenas', 'tortas', 'oil', 'slices', 'persley', 'barley', 'hamentashen', 'homentashen', 'rosquete', 'crabmeat', 'tamarindo', 'tomato', 'hotdog', 'sticks', 'cantaloupe', 'waffle', 'donettes', 'kiwifruit', 'navidenas', 'crab', 'doughnut', 'lollipop', 'jams', 'pop', 'paczki', 'chicharrones', 'enhancer', 'bucatini', 'jawbreakers', 'lolliheart', 'bolillos', 'almond', 'calzone', 'lollypop', 'sausages', 'macadamias', 'mettwurst', 'beverages', 'mangoneada', 'pastrami', 'pumpkins', 'farfalle', 'pepitas', 'zaban', 'pancrepes', 'cashew', 'margherita', 'trout', 'strudels', 'piloncillo', 'hamburgers', 'eclairs', 'slushy', 'tostados', 'gherkins', 'muffuletta', 'pastie', 'gorditas', 'toastees', 'chew', 'mustrad', 'pico', 'focaccibites', 'puree', 'tremocos', 'biologique', 'broccoli', 'blossoms', 'cheeesecake', 'enchiladas', 'masarepa', 'yautia', 'yam', 'cannellini', 'coldfish', 'croquettes', 'skyr', 'gummi', 'bits', 'mirepoix', 'tintern', 'cheesoning', 'provolone', 'hashbrowns', 'salami', 'avocado', 'shake', 'nougat', 'soursop', 'nectars', 'browning', 'superdrink', 'lavender', 'sparkling', 'gomasio', 'elixir', 'hempmilk', 'trinidads', 'grapeade', 'dulse', 'drops', 'balsamic', 'supertea', 'milkis', 'natilla', 'cocopandan', 'pandan', 'fruitcake', 'fortificada', 'morsels', 'splash', 'roquefort', 'aero', 'mint', 'thyme', 'bison', 'frankfurters', 'marigate', 'slice', 'mascarpone', 'babaghannouj', 'custard', 'sacchettini', 'churros', 'spaghettoni', 'milkshake', 'icey', 'rootbeer', 'sliders', 'gelatina', 'firecrackers', 'ceviche', 'carnitas', 'noodle', 'buritto', 'grinder', 'herbamare', 'ollucus', 'octomar', 'browines', 'fragile', 'peppermints', 'stroopwafel', 'clams', 'waffy', 'jellybeans', 'marmalades', 'drinks', 'khichadi', 'flautas', 'zur', 'mazapan', 'tortilleria', 'pepperballs', 'puding', 'butterhorns', 'pieces', 'licuado', 'sweetbread', 'collard', 'nonpareils', 'decors', 'harissa', 'soybeans', 'bolitos', 'chaos', 'hummos', 'dips', 'pizzelle', 'superfruits', 'ratatouille', 'sangria', 'popcron', 'jerky', 'ajvar', 'currants', 'filberts', 'florentines', 'tatalli', 'taralli', 'fettucini', 'onion', 'cayennade', 'nibs', 'panini', 'trufffles', 'trolls', 'apricot', 'refresh', 'snackers', 'guacatillo', 'delinut', 'sugarfina', 'kimchi', 'seeduction', 'multigrain', 'walnut', 'campanelle', 'bouillabaisse', 'tonic', 'chocomaker', 'hunkola', 'queso', 'lasagne', 'grasshopper', 'dairy', 'doughnuts', 'stollen', 'hoagies', 'blend', 'matzo', 'cakebars', 'broccoleaf', 'fattoule', 'linaza', 'cornmeal', 'quencher', 'butterflies', 'caviar', 'ramen', 'guacasalsa', 'coconola', 'telera', 'braeburn', 'butterkase', 'bresaola', 'pancetta', 'pluot', 'chupalicious', 'mediterranean', 'salsacuse', 'hash', 'halibut', 'remoulade', 'stewed', 'sacchetti', 'jamaican', 'breadstick', 'snickerdoodle', 'gummyz', 'garlic', 'smoki', 'palanqueta', 'simplicity', 'gingerose', 'sharks', 'tuscan', 'rye', 'sprinkle', 'estafiate', 'shawarma', 'coconutfudge', 'toasters', 'yellowfin', 'biscoff', 'diet', 'nba2k17', 'watermelon', 'garanola', 'kolita', 'cajeta', 'bonbons', 'babka', 'jalapenos', 'gingerona', 'plain', 'cookedsquash', 'fresa', 'souse', 'zesty', 'classic', 'seafood', 'frankfurts', 'ziti', 'shallots', 'cones', 'spreads', 'pringles', 'crackerfuls', 'tubes', 'chives', 'orecchiette', 'riccioli', 'nocciolata', 'nanche', 'dumpling', 'limon', 'nutcrackers', 'favereds', 'decaffeinated', 'omelet', 'bulghur', 'aloe', 'crumpets', 'skry', 'cheeseburgers', 'concha', 'shreds', 'snackpies', 'cornsticks', 'tabouli', 'galette', 'caserecce', 'butterbread', 'figs', 'sours', 'sauces', 'mounds', 'breads', 'ale', 'medley', 'gems', 'frittata', 'malt', 'cluster', 'habanero', 'seltzerwater', 'salamini', 'coolstix', 'instant', 'protein', 'diabetic', 'sourdougb', 'challab', 'mezzelune', 'goodies', 'bauernwurst', 'smarties', 'nector', 'escarole', 'alfredo', 'meals', 'crunchers', 'kettlecorn', 'bun', 'fusilloni', 'allsorts', 'royale', 'foodles', 'shakes', 'refreshers', 'grattini', 'brie', 'linguini', 'bowls', 'frittatas', 'wholes', 'spears', 'halves', 'tropical', 'grassmilk', 'buttermints', 'cocofudge', 'haystacks', 'cosomi', 'caserecci', 'rizogalo', 'buddha', 'edam', 'masa', 'borscht', 'cordial', 'grenadine', 'cosmopolitan', 'micheladas', 'picante', 'crisp', 'cigar', 'goteborg', 'nougats', 'creamers', 'roux', 'twisties', 'bockwurst', 'challah', 'oysters', 'chilorio', 'tropickles', 'rustica', 'mexicocoa', 'souvlaki', 'turtles', 'cantina', 'puerquitos', 'brevas', 'cannoli', 'saxonshires', 'ranchero', 'montmorency', 'juicebiotics', 'squeezers', 'aspartame', 'lollycones', 'tenders', 'walnutmilk', 'naranjilla', 'gazpacho', 'gaucamole', 'coconut', 'feta', 'mellowafers', 'mystery', 'chicks', 'thins', 'hazelnut', 'kaiser', 'creamsicle', 'amaranth', 'coffeecreamer', 'hamantashen', 'spritzer', 'lumaconi', 'stracciatella', 'profiteroles', 'nori', 'macarons', 'clementeenies', 'springwater', 'macoun', 'clementine', 'meal', 'rutabaga', 'chayote', 'heart', 'radicchio', 'dessert', 'cardamom', 'meat', 'serrano', 'probiotics', 'sunchokes', 'totopos', 'masterpieces', 'palmiers', 'soppressata', 'munchies', 'moodibars', 'macrobar', 'donitas', 'sweetie', 'viennas', 'brookie', 'limes', 'spearmint', 'butterfly', 'granulated', 'gelatins', 'tahinibar', 'limoncello', 'organic', 'food', 'lavash', 'buffalo', 'hotnuts', 'essenza', 'cobettes', 'zucchini', 'graham', 'fruta', 'chicharron', 'zemita', 'golbar', 'mexican', 'dunkelwurst', 'tropicals', 'coffeecake', 'marsala', 'pelati', 'cokos', 'meistersiuger', 'galletas', 'rutabagas', 'chevre', 'haystack', 'meringata', 'disco', 'hazelnuts', 'bubblemint', 'patriots', 'parboiled', 'mini', 'bunny', 'panquecitos', 'radishes', 'bangers', 'leeks', 'papaya', 'saccharin', 'capocollo', 'frosty', 'pitted', 'arrowroot', 'amaretti', 'rellerindos', 'erythritol', 'burritos', 'free food']

	terms_list = ['ice cream', 'cookies', 'cookie', 'pizza', 'pizzas', 'burritos', 'burrito', 'waffle', 'waffles', 'food', 'free food', 'snack', 'snacks', 'boba', 'bagels', 'muffins', 'coffee', 'tea', 'cupcakes', 'chicken', 'taco', 'poke']

	patterns = [nlp.make_doc(text) for text in terms_list]

	matcher.add("phrase_matcher", None, *patterns)



	fictional_char_doc = nlp(email)

	character_matches = matcher(fictional_char_doc)
	food_list = []
	for match_id, start, end in character_matches:
	    span = fictional_char_doc[start:end]
	    if span.text not in food_list:
	    	food_list.append(span.text)
	return food_list

def find_location(email):
	matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

	terms_list = ['Killian', 'Kresge', 'Lobby 13',
	'Lobby 10',
	'Walker',
	'Green building',
	'Stud',
	'Du pont',
	'Lobdell',
	'EC',
	'East Campus',
	'MacGregor',
	'Baker',
	'Stata',
	'Simmons',
	'Maseeh',
	'McCormick',
	'New House',
	'Next House',
	'Westgate',
	'Tang',
	'Student center',
	'Random',
	'Rockwell',
	'Z center',
	'Zeiger Sports & Fitness Center',
	'Burton',
	'tennis courts',
	'Sailing pavilion',
	'CSAIL']

	patterns = [nlp.make_doc(text) for text in terms_list]

	matcher.add("phrase_matcher", None, *patterns)

	fictional_char_doc = nlp(email)

	character_matches = matcher(fictional_char_doc)

	location_list = []

	for match_id, start, end in character_matches:
	    span = fictional_char_doc[start:end]
	    if span.text not in location_list:
	    	location_list.append(span.text)

	p1 = re.compile('building [0-9]{1,2}')
	p2 = re.compile('room [A-Z]{0,2}[0-9]{1,2}[A-Z]{0,2}-[0-9]{3}')
	p3 = re.compile('[A-Z]{1,2}[0-9]{1,2}')
	p4 = re.compile('[A-Z]{0,2}[0-9]{1,2}[A-Z]{0,2}-[0-9]{3}')
	mtch1 = p1.search(email)
	if mtch1 != None:
		if mtch1[0] not in location_list:
			location_list.append(mtch1[0])
	mtch2 = p2.search(email)
	if mtch2 != None:
		if mtch2[0] not in location_list:
			location_list.append(mtch2[0])
	mtch3 = p3.search(email)
	if mtch3 != None:
		if mtch3[0] not in location_list:
			location_list.append(mtch3[0])
	mtch4 = p4.search(email)
	if mtch4 != None:
		if mtch4[0] not in location_list:
			location_list.append(mtch4[0])
	return location_list

def find_time(email):
	doc = nlp(email)
	for ent in doc.ents:
		if ent.label_=='TIME':
			return ent.text
	return ""

def find_date(email):
	doc = nlp(email)
	for ent in doc.ents:
		if ent.label_=='DATE':
			return ent.text
	return ""

def find_date2(email):
	doc = datefinder.find_dates(email)
	for dc in doc:
		return dc
	return ""



email1 = '''
Subject: [Free-food] [free-food] pizza on the 3rd floor of the stud
To: free-foods <free-foods@mit.edu>
 

Outside W20-307
_______________________________________________
Free-foods mailing list
Free-foods@mit.edu
http://mailman.mit.edu/mailman/listinfo/free-foods
'''

email2 = '''
Subject: Happening today at noon! EECS Welcome Event, Part I
 
As you may have seen in our most recent newsletter:
 
Happening today at noon! Our in-person outdoor event: Featuring Sal's Pizza food truck (while supplies last) TODAY, Friday, September 10 from 12-2pm. The truck will be parked outside building 57 (the Alumni Pool) at the corner of Hockfield Court. You'll check in with your phone at the event for contact tracing purposes. Come any time and please know this is event is "say hello, grab, and go"; we don't expect anyone to stay two hours.
 
Please also come to the virtual event: Featuring Undergraduate Officer, Dr. Katrina LaCurts + representatives from opportunities around campus,  Monday, September 13 from 4-5pm. (to be recorded/distributed). Zoom link: https://mit.zoom.us/j/94815083199
 
ALSO: make sure to get registered today! AND, if you are planning to graduate in February, get onto the February degree list by today’s deadline 😊
 
Ellen Reid | she, her, hers
Undergraduate Program Manager
Electrical Engineering and Computer Science (EECS)
Massachusetts Institute of Technology (MIT)
Make an appointment with an EECS Undergraduate Office advisor.
Make an advising appointment with me. Email to make disability accommodations, if needed.
'''

email3 = '''
Hello McCormick!

Hope everyone had a great summer! We'd like to invite you to the first House Meeting tomorrow September 20 from 8-9pm in the Green Living Room. 

This is the agenda for the meeting so far:
1. Welcome + House Gov Intro
2. Permanent Room Reservations*
3. House Team Updates
4. Budget Approval
5. Gym Rules
6. Q&A

*If you submitted a permanent room reservation, either you or someone else on your behalf must be present at the house meeting to confirm the reservation.

Be sure to come by, eat some food, and discuss all things McCormick! This meeting is the perfect time for any McCormick resident to mention any suggestions or concerns you may have. 

​Please email mccormick-secretary@mit.edu if you have an item you would like to be added to the agenda.

See you then!

Adina, Emma, Meenu, Shelby
McCormick House Government Exec
'''
email4 = '''
Tons of extra Breugger's bagels, muffins, and coffee right outside of Kresge

maroon for bc-talk 
ᐧ'''
email5 = '''
Interested in winning cool prizes like a Nintendo Switch, Airpods, or TV??

Come to our GBM today in ***Lobdell***​ (note that the location has changed!) from 8-10 today for lots of poker, food, and prizes 🙂 Note that due to covid restrictions, we're limiting capacity, so attendance will be on a first come, first serve basis with priority who used this form to sign up in advance. 

Also, a gentle reminder that our committee applications are now open! If you love playing poker and want to help organize poker-related events on campus (such as poker tournaments, guest speakers, and educational content), you can apply here.'''

def find_event(email):
	food = find_food(email)
	location = find_location(email)
	time = find_time(email)
	date = find_date(email)
	# print("food", food)
	# print("location", location)
	# print("time", time)
	# print("date", date)
	i=0
	date_formatted = datetime.date.today()
	for day in weekDays:
		if day in date:
			date_formatted = datetime.date.today()
			add = i-date_formatted.weekday()
			if add<0:
				add = add+7
			date_formatted = date_formatted.replace(day=date_formatted.day+add)
		i=i+1
	if 'today' in date.lower():
		date_formatted = datetime.date.today()
	if 'tomorrow' in date.lower():
		date_formatted = datetime.date.today()
		date_formatted = date_formatted.replace(day=date_formatted.day+1)
	# print(date_formatted)
	return 	{"food": food, "location": location, "time": time, "date": date, 'timestamp': date_formatted.isoformat()}


print(find_event(email1))
print(find_event(email2))
print(find_event(email3))
print(find_event(email4))
print(find_event(email5))