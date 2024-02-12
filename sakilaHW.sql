select actor.first_name, actor.last_name from actor join film_actor on actor.actor_id = film_actor.actor_id join film on film.film_id = film_actor.film_id where film.title = "ACADEMY DINOSAUR";

