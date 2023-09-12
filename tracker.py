import json

def load_json(filename):
    """Load and return JSON data from the given filename."""
    with open(filename) as file:
        return json.load(file)

def get_usernames_from_relationship(relationship):
    """Extract usernames from relationship data."""
    return [entry["string_list_data"][0]["value"] for entry in relationship]

# Load JSON data
following_json = load_json('following.json')
followers_json = load_json('followers_1.json')

# Extract the list of people being followed and the list of followers
people_following = set(get_usernames_from_relationship(following_json["relationships_following"]))
followers = set(get_usernames_from_relationship(followers_json["relationships_followers"]))

# Calculate the difference to get the list of people who unfollowed
people_not_following_back = people_following - followers

print("LIST OF PEOPLE WHO UNFOLLOWED ME:")
for user in people_not_following_back:
    print("- " + user)
