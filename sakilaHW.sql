select actor.first_name, actor.last_name from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id where film.title = "ACADEMY DINOSAUR";

select category.name, count(*) from category join film_category where category.category_id = film_category.category_id group by category.category_id;

select rating, AVG(rental_duration) from film group by rating;

select customer.first_name, customer.last_name, count(rental.rental_id) from customer join rental on customer.customer_id = rental.customer_id group by customer.customer_id;

select customer.store_id, count(rental.rental_id) from customer join rental on customer.customer_id = rental.customer_id group by customer.store_id order by count(rental.rental_id) desc limit 1;
