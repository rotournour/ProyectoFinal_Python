Hola! Soy Rocio Tournour, tengo 25 años y soy Licenciada en Organización Industrial. Actualmente estoy desarrollando mi proyecto final de Python en Coderhouse.

El proyecto en cuestion se llama Vintage Store, es una plataforma que fomenta la moda sostenible a traves de la compra y venta de prendas de segunda mano, permitiendo combatir la contaminacion textil con la reutilizacion de todas aquellas prendas que las personas no usan mas.
Para realizar el proyecto, se planteo el siguiente esquema en Django:
1. Se realizo un proyecto con el nombre de proyecto_final donde contenia las configuraciones (settings.py) necesarias del proyecto, las vistas (views.py) con la creacion el index y las urls (urls.py) para mostrar la pagina hacia las personas.
2. Para una mayor comprension y organizacion del proyecto, se plantearon dos aplicaciones (Sales y Clothes), donde las mismas fueron debidamente instaladas en las configuraciones del proyecto (settings.py) para comenzar a trabajar.
3. La aplicacion Clothes, en su apartado de modelos (models.py), contiene tres clases distintas con sus respectivos atributos, las mismas son: Clothes, Type_clothing y Gender. Basicamente, Type_clothing (tipo de ropa: pantalon, remera, etc) y Gender (genero de la ropa: Mujer, Hombre y unisex) se crearon para predefinir los datos desde el admin de django, con el objetivo que el usuario no tenga que escribirlos al momento de vender o comprar su prenda. En tanto, la clase Clothes posee la informacion necesaria de la prenda, dos de sus atributos reciben la informacion brindada por Type_clothing y Gender a traves de un Foreighkey.
4. Mientras que la aplicacion Sales en su apartado de modelos (models.py), posee dos clases: Sales y Payment. Por un lado, Payment posee informacion predefinida desde el admin de Django y Sales contiene la informacion necesaria para llevar a cabo la compra de la prenda, con el atributo sales.payment heredado desde la class Payment a traves de un Foreighkey y sales.category heredada de la clase Type_clothing perteneciente a la app Clothes. Todo esto fue migrado con exito hacia la base de datos con sus respectivas tablas.
5. Bien, una vez realizadas las clases, se comenzo a plantear las vistas. En la app Clothes, se planteo la view create_clothing que realizaba la publicacion de la prenda para su venta, list_categories para mostrar las categorias de prendas que poseia la pagina para su venta y list_clothes para listar las prendas disponibles para su venta. Por otro lado, en la app Sales se planteo la siguiente vista: create_order para realizar la compra de una prenda. 
6. Al mismo tiempo, mientras que se realizaban las views, por cada una se iba confeccionando su respectiva url para que esa view sea funcional y pueda ser mostrada hacia el usuario.
7. Una vez hecho todo lo anterior, se comenzaron a plantear los forms teniendo en cuenta las views confeccionadas y las clases creadas en models. Los forms nos permitiran que la informacion sea cargada por el usuario hacia la base de datos. 
8. Una vez conocidas las views, sus respectivas url y los forms, se creo la carpeta templates y se instalo en el settings del proyecto. La carpeta templates contiene todas las plantillas que se usaran para mostrar la informacion de la pagina en la pantalla, para que el usuario pueda navegar en ella. La carpeta se dividio en las apps para una mejor organizacion. Bien, en primer lugar, se confecciono la template base.html que contiene la navbar para una mejor navegacion y un footer con informacion de utilidad. Esta template fue heredada hacia las templates de cada view. Tambien, se confecciono una template index.html para mostrar el menu principal de la pagina.
9. La aplicacion Clothes posee 3 templates: create.html para la venta del producto, list_categories.html para listar las categorias de las prendas y list_clothes.html para mostrar las prendas disponibles para su venta. En tanto, la aplicacion Sales posee una template llamada order.html para hacer tu compra de alguna prenda disponible.
10. Es muy importante aclarar que views, url y templates estan conectados entre si.
11. Tambien, y no menos importante, se creo el admin en el panel de administracion de Django y se migro todos los modelos con sus clases. En este apartado, se logro que el admin quede legible y organizado para poder operar dentro. En este admin se cargo los tipos de prendas, el genero de la prenda y el tipo de pago, ya que se considero que estos son cargados por el administrador y el usuario solamente elige esa informacion al momento de vender o comprar.


Explicacion de las funcionalidades de la pagina

Al momento de entrar a la pagina, la misma se ubica en su menu principal, donde se puede ver una navbar con breadcrums que permiten el conocimiento del usuario de todas sus funciones permitiendo clickear y dirigirse hacia ellas, y un buscador para agilizar la navegacion por el nombre de las prendas disponibles. A su vez, posee un footer con informacion y otros atajos.
Comenzando por la navbar, si se clickea el nombre 'Vintage Store' este nos llevara al menu principal. A su vez, en el primer atajo ubicado a la derecha, se puede ver las Categorias, en la misma se veran los tipos disponibles de prendas en la pagina, con links que te llevan directo a la compra o venta. Siguiendo, se puede ver Publica tus prendas, aqui se podra vender la ropa que ya no uses. A su derecha se ve Compra tus prendas, aqui se puede hacer el pedido de alguna prenda de la pagina y por ultimo, la Ropa Disponible, aqui se puede navegar por la ropa disponible que posee la pagina con su nombre, precio, categoria, si la prenda es nueva o usada y si existe stock de la misma. En los atajos de publica tus prendas y compra tus prendas existe, para cada una, un formulario donde el usuario puede cargar la informacion necesaria.
