select actor.first_name, actor.last_name from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id where film.title = "ACADEMY DINOSAUR";

select category.name, count(*) from category join film_category where category.category_id = film_category.category_id group by category.category_id;

select rating, AVG(rental_duration) from film group by rating;

select customer.first_name, customer.last_name, count(rental.rental_id) from customer join rental on customer.customer_id = rental.customer_id group by customer.customer_id;

select customer.store_id, count(rental.rental_id) from customer join rental on customer.customer_id = rental.customer_id group by customer.store_id order by count(rental.rental_id) desc limit 1;

select category.name, count(rental.rental_id) from rental join inventory on rental.inventory_id = inventory.inventory_id join film_category on inventory.film_id = film_category.film_id join category on film_category.category_id = category.category_id group by category.name order by count(rental.rental_id) desc limit 1;

select category.name, AVG(film.rental_rate) from film join film_category on film.film_id = film_category.film_id join category on film_category.category_id = category.category_id group by category.name;

select film.title, max(rental.rental_date) from film left join inventory on film.film_id = inventory.film_id left join rental on inventory.inventory_id = rental.inventory_id where rental.rental_date < DATE_SUB(NOW(), INTERVAL 1 MONTH) group by film.title;

select customer.first_name, customer.last_name, SUM(payment.amount) from customer join payment on customer.customer_id = payment.customer_id group by customer.customer_id;

select language.name, AVG(film.length) from film join language on film.language_id = language.language_id group by language.name;
