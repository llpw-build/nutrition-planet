def bag_contents(request):
    bag = request.session.get("bag", {})
    bag_count = sum(bag.values())

    return {
        "bag_count": bag_count,
    }