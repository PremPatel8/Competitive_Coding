
import distance
from sklearn.cluster import AffinityPropagation
import numpy as np

words = ["(Blood Blockade Battlefront, Ep 1)",
         "(My Hero Academia: Heroes Rising)",
         "(My Hero Academia, Ep 76)",
         "(Flip Flappers, NCOP)",
         "(Mob Psycho 100, OP)",
         "(Jujutsu Kaisen, OP)",
         "(Jujutsu Kaisen, OP)",
         "(Promare)",
         "(?) (Mob Psycho 100 II, OP)",
         "([Hero Cantare] Story Trailer Full ver.)",
         "(Fire Force, NCOP1)",
         "(Gurren Lagann, NCOP1)",
         "(Mob Psycho 100 II, OP)",
         "(Soul Eater, NCED1)",
         "(Fire Force, Ep 1)",
         "(Blade Smash CM)",
         "(Macross Card Fighter CM)",
         "(Macross Card Fighter CM)",
         "(Macross Card Fighter CM)",
         "(?) (Inishie no Megami to Houseki no Ite PV)",
         "(Blade Smash CM)",
         "(Deca-Dence, Ep 1)",
         "(Hades Launch Trailer)",
         "(Hades Launch Trailer)",
         "(Hades Launch Trailer)",
         "(Kaze no Yojimbo, Pachislot OP)",
         "(My Hero Academia: Heroes Rising)",
         "(Fate/Grand Order Absolute Demonic Front: Babylonia, Ep 18)",
         "(Star Driver the Movie)",
         "(Star Driver the Movie)",
         "(To Be Heroine, Ep 3)",
         "(Devilman Crybaby, Ep 1)",
         "(Star Driver, Ep 12)",
         "(Dolls Order OP)",
         "(Eureka Seven: Hi-Evolution, Movie 1)",
         "(Evangelion 1.11)",
         "(Evangelion 2.22)",
         "(Eureka Seven, NCOP2)",
         "(Guilty Crown, NCOP1)",
         "(Blood Blockade Battlefront & Beyond, Ep 5)",
         "(Boogiepop wa Warawanai PV)",
         "(The Seven Deadly Sins: Revival of The Commandments, NCOP2)",
         "(raison d’etre − Eve MV)",
         "(Azur Lane 3rd Anniversary CM)",
         "(Cyphers CM)",
         "(Jujutsu Kaisen, OP)",
         "(Boruto, NCOP4)",
         "(Inishie no Megami to Houseki no Ite PV)",
         "(Pokémon Twilight Wings, Ep 7)",
         "(?) (Pokémon Twilight Wings, Ep 7)",
         "(Pokémon Twilight Wings, Ep 7)",
         "(Pokémon Twilight Wings, Ep 7)",
         "(Promare)",
         "(Origin: Spirits of the Past)",
         "(Eureka Seven: Hi-Evolution, Movie 1)",
         "(Attack on Titan, Ep 39)",
         "(Gurren Lagann Movie 1)",
         "(Attack on Titan, NCOP5)",
         "(Bleach, Ep 341)",
         "(Bleach: Hell Verse)",
         "(Fire Force, NCOP1)",
         "(Jujutsu Kaisen, OP)",
         "(Dragon Ball Z: Battle of Gods)",
         "(Dragon Ball Super: Broly)",
         "(?) (Princess Connect! Re:Dive, NCOP)",
         "(One Piece, Ep 934)",
         "(Sirius the Jaeger, Ep 2)",
         "(Sirius the Jaeger, Ep 1)",
         "(Sirius the Jaeger, Ep 2)",
         "(Rise of the Teenage Mutant Ninja Turtles, Ep 39b)",
         "(Fate/stay night: Heaven's Feel II. Lost Butterfly)",
         "(Fate/stay night: Heaven's Feel II. Lost Butterfly)",
         "(Konosuba 2, Ep 10)",
         "(Fate/stay night: Heaven's Feel II. Lost Butterfly)",
         "(Flip Flappers, Ep 12)",
         "(Fate/stay night: Heaven's Feel II. Lost Butterfly)",
         "(Gurren Lagann Movie 2)",
         "(Fireworks)"]


print(sorted(words))

# words = "YOUR WORDS HERE".split(" ")  # Replace this line
""" words = np.asarray(words)  # So that indexing with a list will work
lev_similarity = -1*np.array([[distance.levenshtein(w1, w2)
                               for w1 in words] for w2 in words])

affprop = AffinityPropagation(affinity="precomputed", damping=0.5)
affprop.fit(lev_similarity)
for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_ == cluster_id)])
    cluster_str = ", ".join(cluster)
    print(" - *%s:* %s" % (exemplar, cluster_str))
 """