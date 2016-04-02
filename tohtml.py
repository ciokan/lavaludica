import re
import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('lavaludica.xml').getroot()

ct = 0
for atype in e.findall('Record'):
	if ct != 0:
		price = atype[0].attrib['E']
		product_name = atype[0].attrib['D']
		article_no = atype[0].attrib['C']
		description = atype[0].attrib['F']
		selling_points = atype[0].attrib['G']
		deliverytime = atype[0].attrib['H']
		materials = atype[0].attrib['I']
		colors = atype[0].attrib['J']
		product_details = atype[0].attrib['K']
		clean_wash = atype[0].attrib['L']
		country_origin = atype[0].attrib['M']
		dimensions = atype[0].attrib['N'] if 'N' in atype[0].attrib else 0
		height = atype[0].attrib['O'] if 'O' in atype[0].attrib else 0
		weight = atype[0].attrib['P']

		tpl = """
<div class="column">
	<div class="ui fluid link card" data-cardid="{id}">
		<div class="image">
			<b class="ui orange ribbon label">{article_no}</b>
			<img src="{image}">
		</div>
		<div class="content">
			<div class="header">{name}</div>
			<div class="meta">
				<a>{category}</a>
			</div>
			<div class="description">
				{description}
			</div>
		</div>
		<div class="extra content">
			<span class="right floated popup" data-content="Multicolored" data-variation="inverted">
				<b class="ui red empty circular label"></b>
				<b class="ui orange empty circular label"></b>
				<a class="ui violet empty circular label"></a>
				<b class="ui olive empty circular label"></b>
				{colors}
			</span>
			<span>
				<i class="euro icon"></i>
				{price}
			</span>
		</div>
	</div>

	<div class="ui modal" id="{id}">
		<i class="close icon"></i>
		<div class="header">{name}</div>
		<div class="image content">
			<div class="image"><img src="{image}"></div>
			<div class="description" style="width: 100%">
				{description}
				<br/>
				<div class="ui icon info message">
					<i class="heart icon"></i>
					<div class="content">
						<div class="header">
							Hand-made with love in {origin}
						</div>
						<p>{selling_points}</p>
					</div>
				</div>
			</div>
		</div>

		<div class="actions">
			<b>Price:</b> {price} euro &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<b>Est. deliverytime:</b> {deliverytime} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<b>Materials:</b> {materials} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<b>Weight (grams):</b> {weight}
		</div>
	</div>
</div>
"""

		print(tpl.format(**{
			'image': './static/chairs/image%d.jpeg' % ct,
			'materials': materials,
			'article_no': article_no,
			'weight': weight,
			'name': product_name.replace("_", "-"),
			'category': '',
			'description': description,
			'colors': '',
			'price': price,
			'deliverytime': deliverytime,
			'origin': country_origin,
			'selling_points': selling_points,
			'id': re.sub(r'\W+', '', article_no).lower()
		}))

	ct += 1
