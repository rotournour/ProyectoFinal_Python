Hola! Soy Rocio Tournour, tengo 25 años y soy Licenciada en Organización Industrial. Actualmente estoy desarrollando mi proyecto final de Python en Coderhouse.

El proyecto en cuestión se llama Vintage Store, es una plataforma que fomenta la moda sostenible a través de la compra y venta de prendas de segunda mano, permitiendo combatir la contaminación textil con la reutilización de todas aquellas prendas que las personas no usan más. Para realizar el proyecto, se planteo el siguiente esquema en Django:

1. Se creo un proyecto con el nombre de proyecto_final donde contiene las configuraciones (settings.py) necesarias del proyecto, las vistas (views.py) con la creación el index y las urls (urls.py) para mostrar la página hacia las personas.
2. Para una mayor comprensión y organización del proyecto, se plantearon dos aplicaciones (Sales y Clothes), donde las mismas fueron debidamente instaladas en las configuraciones del proyecto (settings.py) para comenzar a trabajar.
3. La aplicación Clothes, en su apartado de modelos (models.py), contiene tres clases distintas con sus respectivos atributos, las mismas son: Clothes, Type_clothing y Gender. Basicamente, Type_clothing (tipo de ropa: pantalón, remera, etc.) y Gender (género de la ropa: Mujer, Hombre y unisex) se crearon para predefinir los datos desde el admin de django, con el objetivo que el usuario no tenga que escribirlos al momento de vender o comprar su prenda. En tanto, la clase Clothes posee la información necesaria de la prenda, donde dos de sus atributos reciben la información brindada por Type_clothing y Gender a través de un Foreighkey.
4. Mientras que la aplicación Sales en su apartado de modelos (models.py) posee dos clases: Sales y Payment. Por un lado, Payment posee información predefinida desde el admin de Django y Sales contiene la información necesaria para llevar a cabo la compra de la prenda, con el atributo sales.payment heredado desde la class Payment a través de un Foreighkey y sales.category heredada de la clase Type_clothing perteneciente a la app Clothes. Todo esto fue migrado con éxito hacia la base de datos con sus respectivas tablas.
5. Bien, una vez realizadas las clases, se comenzó a plantear las vistas. En la app Clothes, se planteo la view create_clothing que carga la publicación de la prenda para su venta, list_categories para mostrar las categorías de prendas que posee la página para su venta y list_clothes para listar las prendas disponibles para su venta. Por otro lado, en la app Sales se planteo la siguiente vista: create_order para realizar la compra de una prenda.
6. Al mismo tiempo, mientras que se confeccionaban las views, por cada una se iba confeccionando su respectiva url para que esa view sea funcional y pueda ser mostrada hacia el usuario.
7. Una vez hecho todo lo anterior, se comenzaron a plantear los forms teniendo en cuenta las views confeccionadas y las clases creadas en models. Los forms nos permitirán que la información sea cargada por el usuario hacia la base de datos.
8. Una vez conocidas las views, sus respectivas url y los forms, se creo la carpeta templates y se instalo en el settings del proyecto. La carpeta templates contiene todas las plantillas que se usaran para mostrar la información de la página en la pantalla, para que el usuario pueda navegar en ella. La carpeta se dividió en las apps para una mejor organizacion. Bien, en primer lugar, se confecciono la template base.html que contiene la navbar para una mejor navegación y un footer con información de utilidad. Esta template fue heredada hacia las templates de cada view. También, se confecciono una template index.html para mostrar el menú principal de la página.
9. La aplicación Clothes posee 3 templates: create.html para la venta del producto, list_categories.html para listar las categorias de las prendas y list_clothes.html para mostrar las prendas disponibles para su venta. En tanto, la aplicacion Sales posee una template llamada order.html para hacer tu compra de alguna prenda disponible.
10. Es muy importante aclarar que views, url y templates están conectados entre si.
11. También, y no menos relevante, se creo el admin en el panel de administración de Django y se migro todos los modelos con sus clases. En este apartado, se logro que el admin quede legible y organizado para poder operar dentro. En este admin se cargo los tipos de prendas, el género de la prenda y el tipo de pago, ya que se considero que estos son cargados por el administrador y el usuario solamente elige esa información al momento de vender o comprar.

Explicación de las funcionalidades de la página

Al momento de entrar a la página, la misma se ubica en su menú principal, donde se puede ver una navbar con breadcrums que permiten el conocimiento del usuario de todas sus funciones, permitiendo cliquear y dirigirse hacia ellas, y un buscador para agilizar la navegación por el nombre de las prendas disponibles. A su vez, posee un footer con información y otros atajos. Comenzando por la navbar, si se cliquea el nombre 'Vintage Store' este nos llevará al menú principal. A su vez, en el primer atajo ubicado a la derecha, se puede ver las Categorías, en la misma se verán los tipos disponibles de prendas en la página, con links que te llevan directo a la compra o venta. Siguiendo, se puede ver Publica tus prendas, aquí se podrá vender la ropa que ya no uses. A su derecha se ve Compra tus prendas, aquí se puede hacer el pedido de alguna prenda de la página y por último, la Ropa Disponible, aquí se puede navegar por la ropa disponible que posee la página con su nombre, categoría, marca, precio, si la prenda es nueva o usada y si existe stock de la misma. En los atajos de publica tus prendas y compra tus prendas existe, para cada una, un formulario donde el usuario puede cargar la información necesaria.

