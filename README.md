# logo_page_classifier
Tool to classify pages as logo pages or not (partners, customers, etc.)

## Goal

The goal of this project is to recognize logo pages, via a classifier. Logo pages are partnership or example customer pages.

## Feature Extraction

The bulk of the work will be feature extraction: figuring out what about a web page signals that it is a logo page or not. Three signals that seem good are:

* Do 'partner','alliance' or 'customer' appear in the url?
* How many external links are present?
* How many known company names appear in the page?

It is convenient to create libraries that can be executred on arbitrary input as command line tools. These tools should return json, which can then be loaded into sklearn.

### Keywords in URL

See [features/url.py](features/url.py)

#### Command Line

```
$ features/url.py aallianceaagpartneraapartnerallianceacustomera
{"match_count": 5, "matches": ["alliance", "partner", "partner", "alliance", "customer"]}

$ features/url.py aagag
{"match_count": 0, "matches": []}
```

#### Library

```
def match_keyword(url):

  regex = re.compile('(partner|alliance|customer)', flags=re.I)
  matches = regex.findall(url)

  return {'match_count': len(matches), 'matches': matches}
```

To use:

```
from url import match_keyword
match_keyword(my_url)
```

## Classification

Decision trees should work well here. See sklearn and its decision trees http://scikit-learn.org/stable/modules/tree.html