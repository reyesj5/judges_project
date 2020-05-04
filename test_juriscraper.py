from juriscraper.opinions.united_states.federal_appellate import ca1

# Create a site object
site = ca1.Site()

# Populate it with data, downloading the page if necessary
site.parse()

# Print out the object
print str(site)

# Print it out as JSON
print site.to_json()

# Iterate over the item
for opinion in site:
        print opinion
