# Les Différentes clauses du langage SQL
>TRES IMPORTANT => toute fin d'instruction en SQL se termine par un " ; "  

## SELECT
>Cette clause sert à retourner un ou des élément (avec ou sans conditions) dans une table  

    SELECT * FROM table; => TOUTES les colonnes de la table  
    SELECT colone1, colonne2 FROM table; => La colonne 1 et 2 de la table  
    SELECT DISTINCT colone1 FROM table; => La clause DISTINCT sert à avoir les différentes colone1 sans répéter les doublons.  

## WHERE
>La clause WHERE définis une condition bien précise  

    SELECT name, address FROM user
        WHERE name='joe';
    (ou)WHERE name='julien' AND age<50;
    (ou)WHERE name='marie' OR name='pierre';
 
>Les opérateurs sont:  
    = égal à ...  
    > plus grand que ...  
    >= plus grand ou égal à ... 
    < plus petit que ... 
    <= plus petit ou égal à ...  
    <> ou != différent de ...  
    AND opérateur logique ET
    OR opérateur logique OU

## AS
>Renommer temporairement dans la même instruction une colonne ou table dans le but de différencier ou de clarifier les données que l'on manipule

	SELECT name AS 'user_name', age AS 'user_age' FROM user;

## COUNT
>Donne le nombre total d'éléments de la table

	SELECT COUNT * FROM table;

>Ou le nombre total d'éléments de la colonne1 sans les valeurs NULL

	SELECT COUNT colonne1 FROM table;

>Ou le nombre total d'éléments sans les doublons avec la clause DISTINCT.

	SELECT COUNT (DISTINCT colonne1) FROM table;

## LIMIT
>Retourne les 'n' premiers éléments d'une table, ici les 5 premiers

    SELECT name FROM  table LIMIT 5;

## ORDER BY
>Trie les éléments selon une colonne, ici la colonne name de manière ascendante (par défaut) ASC donc de A à Z.

	SELECT name, age FROM user ORDER BY name;

>Ou de manière descendante DESC de Z à A.

    ... ORDER BY name DESC;

>Il est possible d'afficher une colonne en fonction d'une autre qui n'est pas affichée mais néanmoins triée

    SELECT name FROM user ORDER BY age;

## LIKE
>Sélectionne les éléments dont le début commence par 'm' et sont suivis par autre chose d'où le '%' ou qui finissent par 'm' mais précédés par autre chose '%m' ou encore dont le deuxième élément est un 'm' soit '_m%'.

	SELECT name, address FROM user WHERE name LIKE 'm%';

## IN
>Evite les clauses OR ou AND à répétition, par exemple ici on évite d'écrire  
>WHERE age=20 OR age=21 OR age=22 OR age=23 OR age=24 OR age=25;  
>Il est possible d'y ajouter NOT devant pour écarter toute les valeurs comprise dans cette intervalle avec NOT IN.

	SELECT name, age FROM user WHERE age 
	IN (20,21,22,23,24,25) ORDER BY name DESC;

## BETWEEN
>Sélectionner les éléments compris dans un interval de valeurs, on peut aussi exclure avec NOT BETWEEN.

	SELECT name, address FROM user WHERE age BETWEEN 6 AND 12;

## AVG
>Avoir la moyenne totale de tout les éléments d'une table ou portion grâce à la clause WHERE. On arrondis avec ROUND au besoin.

	SELECT AVG age FROM user;
	SELECT ROUND(AVG(price),2) FROM sale;

        SUM pour la somme.
        MAX pour le maximum.
        MIN pour le minimum.
        -> On appelle ces clauses 'les Agrégations'.

## GROUP BY
>Regroupe sous l'agrégation voulu, ici le total des achats, par utilisateur. Si aucune agrégation n'est utilisée il faut grouper par les même colonnes utilisées que pour le SELECT:

	SELECT user_name, ROUND(SUM(sale_price), 2) FROM sale GROUP BY user_name;
	SELECT user_name, sale_price FROM sale GROUP BY user_name, sale_price;

>Ici on veut retourner les users groupés selon la moyenne de leurs achats triés du plus grand montant au plus bas, '2' faisant référence ici à 'AVG(sale_price)'

    SELECT user_name, AVG(sale_price) FROM sale
	GROUP BY user_name ORDER BY 2 DESC;

## HAVING
>S'utilise sur des groupes à l'inverse de WHERE qui s'utilise sur des lignes sert a sélectionner une portion dans un groupe donné, ici par exemple on veut les users qui ont dépensés plus de 200 euros dans le groupe que l'on a crée.

	SELECT user_name, ROUND(SUM(sale_price), 2) FROM sale GROUP BY user_name
	HAVING ROUND(SUM(sale_price), 2) > 200;

## Les sous-requêtes
>Ici nous avons un exemple simple de sous-requête. Elles sont très utiles afin d'économiser du temps et de l'énergie en termes d'opérations.

	SELECT user_name, sale_price FROM sale
	WHERE sale_price > (SELECT AVG(sale_price) FROM sale);

## INSERT INTO
>Insérer des valeurs dans une table.

	INSERT INTO user(name, address, tel)
	VALUES('Joe', '10 rue du fion 75000 Paris', '555-623-458');

>On peut aussi créer plusieurs lignes d'un coup:

	INSERT INTO user(name, address, tel)
	VALUES('Joe', '10 rue du fion 75000 Paris', '555-623-458'),
		  ('Jennifer', '8 avenue des nibards 9100 Evry', '588-624-558'),
		  ('Marc', '25 rue du zgeg 45000 Montargis', '356-233-878');

## UPDATE
>Changer les valeurs d'une' colonne.

	UPDATE user
	SET colonne1='nouvelle valeur'
	WHERE colonne2='valeur';

## DELETE
>Supprimer les valeurs d'une colonne.

	DELETE FROM user
	WHERE age=10;

## ALTER
>Modifier selon le critère une table.

	ALTER TABLE user
		ADD COLUMN 'nouvelle_colonne';
        (ou)DROP COLUMN 'name';
        (ou)RENAME COLUMN 'age';
        (ou)ADD CONSTRAINT;
        (ou)RENAME COLUMN 'address';

## DROP TABLE
>Supprimer une table, IF EXIST permet d'éviter une erreur si la table n'existe pas

	DROP TABLE IF EXIST users;

## JOINTURES
>Les jointures sont la puissance des bases de données dites relationnelles. Elles permettent de regrouper des requêtes faites sur des tables différentes en une seule et unique requête, permettant ainsi un gain de temps et d'économie.

### Voici les différents types de jointures:

![les_jointures.png](/les_jointures.png "Les Différents Types de Jointures")