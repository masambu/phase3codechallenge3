class Customer:
    """
    Represents a customer who can leave reviews for restaurants.
    """

    all = []  # List to store all instances of customers

    def __init__(self, first_name, last_name):
        """
        Initializes a new instance of the Customer class.

        Args:
            first_name (str): The first name of the customer.
            last_name (str): The last name of the customer.
        """
        self.first_name = first_name
        self.last_name = last_name
        Customer.all.append(self)

    @property
    def first_name(self):
        """str: The first name of the customer."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Sets the first name of the customer.

        Args:
            value (str): The first name to set.
        """
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value

    @property
    def last_name(self):
        """str: The last name of the customer."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Sets the last name of the customer.

        Args:
            value (str): The last name to set.
        """
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value

    def reviews(self):
        """
        Returns a list of all reviews made by this customer.
        """
        return [review for review in Review.all if review.customer == self]

    def restaurants(self):
        """
        Returns a list of restaurants reviewed by this customer.
        """
        return list(set([review.restaurant for review in self.reviews()]))

    def num_negative_reviews(self):
        """
        Returns the number of negative reviews (ratings 2 or less) made by this customer.
        """
        return len([review for review in self.reviews() if review.rating <= 2])

    def has_reviewed_restaurant(self, restaurant):
        """
        Checks if the customer has reviewed a specific restaurant.

        Args:
            restaurant (Restaurant): The restaurant to check for review.

        Returns:
            bool: True if the customer has reviewed the restaurant, False otherwise.
        """
        return any(review.restaurant == restaurant for review in self.reviews())


class Restaurant:
    """
    Represents a restaurant that can be reviewed by customers.
    """

    all = []  # List to store all instances of restaurants

    def __init__(self, name):
        """
        Initializes a new instance of the Restaurant class.

        Args:
            name (str): The name of the restaurant.
        """
        self.name = name
        Restaurant.all.append(self)

    @property
    def name(self):
        """str: The name of the restaurant."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the restaurant.

        Args:
            value (str): The name to set.
        """
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value

    def reviews(self):
        """
        Returns a list of all reviews received by this restaurant.
        """
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        """
        Returns a list of customers who have reviewed this restaurant.
        """
        return list(set([review.customer for review in self.reviews()]))

    def average_star_rating(self):
        """
        Computes the average star rating of this restaurant based on received reviews.

        Returns:
            float: The average star rating.
        """
        ratings = [review.rating for review in self.reviews()]
        if not ratings:
            return 0.0
        return round(sum(ratings) / len(ratings), 1)

    @classmethod
    def top_two_restaurants(cls):
        """
        Returns the top two restaurants based on average star ratings.

        Returns:
            list: A list containing the top two restaurants.
        """
        sorted_restaurants = sorted(
            cls.all,
            key=lambda restaurant: restaurant.average_star_rating(),
            reverse=True
        )
        return sorted_restaurants[:2]


class Review:
    """
    Represents a review given by a customer to a restaurant.
    """

    all = []  # List to store all instances of reviews

    def __init__(self, customer, restaurant, rating):
        """
        Initializes a new instance of the Review class.

        Args:
            customer (Customer): The customer who gave the review.
            restaurant (Restaurant): The restaurant being reviewed.
            rating (int): The rating given by the customer (1 to 5 stars).
        """
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all.append(self)

    @property
    def rating(self):
        """int: The rating given by the customer."""
        return self._rating

    @rating.setter
    def rating(self, val):
        """
        Sets the rating of the review.

        Args:
            val (int): The rating to set.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        if isinstance(val, int) and 1 <= val <= 5 and not hasattr(self, '_rating'):
            self._rating = val

    @property
    def customer(self):
        """Customer: The customer who gave the review."""
        return self._customer

    @customer.setter
    def customer(self, val):
        """
        Sets the customer who gave the review.

        Args:
            val (Customer): The customer to set.
        """
        if isinstance(val, Customer):
            self._customer = val

    @property
    def restaurant(self):
        """Restaurant: The restaurant being reviewed."""
        return self._restaurant
