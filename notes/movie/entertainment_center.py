import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A story of y boy and his toys that come to life", 
						"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://www.impawards.com/2009/posters/avatar.jpg",
					 "https://www.youtube.com/watch?v=8TNlvM4cN6U")

lotr1 = media.Movie("Der Herr der Ringe: Die Gefaehrten",
				   "Die Gefaehrten erzaehlt zunaechst die Vorgeschichte des sogenannten Einen Rings...",
				   "http://f-cdn.filmjunkies.de/film/191/poster/herr-ringe-gefaehrten-54769.jpg",
				   "https://www.youtube.com/watch?v=dysvOlKkZYE")

lotr2 = media.Movie("Der Herr der Ringe: Die zwei Tuerme",
				   "In drei Gruppen zerstreut, stemmen sich die Gefaehrten gegen Mordor...",
				   "http://is4.mzstatic.com/image/pf/us/r30/Video/43/ea/04/mzi.pbmkkemn.jpg",
				   "https://www.youtube.com/watch?v=YpvecCQ-GA4")

lotr3 = media.Movie("Der Herr der Ringe: Die Rueckkehr des Koenigs",
				   "Die letzte Schlacht um Mittelerde beginnt...",
				   "http://is5.mzstatic.com/image/pf/us/r30/Video/de/c6/c1/mzi.tskkgdyz.jpg",
				   "https://www.youtube.com/watch?v=7mGY7AVPmKk")

gravity = media.Movie("Gravity",
				   "Sandra Bullock und George Clooney spielen die Hauptrollen in diesem Thriller, bei dem man Herzklopfen bekommt...",
				   "http://is4.mzstatic.com/image/pf/us/r30/Video6/v4/79/e9/c1/79e9c113-6504-d0b9-509f-635316cc31c2/mza_2509991788517230101.jpg",
				   "https://www.youtube.com/watch?v=VNUMREIIM_8")


movies = [toy_story, avatar, lotr1, lotr2, lotr3, gravity]
fresh_tomatoes.open_movies_page(movies)