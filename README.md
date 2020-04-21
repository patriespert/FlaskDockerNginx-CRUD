# FlaskDockerNginx-CRUD

<b>INSTRUCCIONES PARA EJECUTAR EN WINDOWS</b>

<ul>
  <li>Accedemos desde el navegador a <b> http://nginx.org/en/download.html </b> y bajamos en <b> MAINLAINE VERSION  la opcion que ponga     /windows </b> <u>Se nos bajará un archivo.zip que vamos a descomprimir con WinRar en la raiz del sistema (c:\) y le cambiamos el nombre   a la carpeta resultante --> nginx (a secas) </u> <br></li>
  <li> <u> Una vez hecho todo esto </u> nos a la CMD (escribimos cmd en cortana) </li>
  <li> desde cmd vamos a escribir cd c:\nginx, una vez dentro de esa carpeta escribimos nginx (inmediatamente se ejecutará y estará        corriendo en nuestro equipo) </li>
  <li> <b> En el escritorio de Windows </b> generamos una carpeta y le ponemos el nombre que queramos</li>
  <li>Bajamos git y nos metenemos en git BASH</li>
  <li>En git bash escribimos <b> pwd </b> para situarnos y despues cd Desktop/"<nombre-carpeta>" siendo "<nombre-carpeta>" el nombre que le hemos dado a la misma</li>
   <li> Dentro de esta carpeta escribimos git clone https://github.com/patriespert/FlaskDockerNginx-CRUD.git . (<b>MUY IMPORTANTE PONER EL   '.' AL FINAL </b>) </li>
    <li> Ahora  <b> escribimos ls -a y nos aseguramos de que exista el fichero docker-compose.yml </b> </li>
    <li> Una vez hecha esta comprobación vamos a escribir <b> docker-compose up --build </b> </li>
    <li> todo sale bien,  <u> al escribir docker-ps nos tienen que aparecer 3 contenedores </u> > </li>
    <li> Ahora en el navegador escribimos localhost:5000 et voilá ya estamos en la aplicación! </li>
    <hr/>
    <li>Con todo esto seguimos en el mismo directorio (Desktop/<nombre-carpeta>) y escribimos  <b>docker exec -it <id del contenedor de mysql> bash </b> </li>
    <li> Se nos abrirá un prompt de mysql y  <b> escribimos mysql -u admin -p mydb </b> </li>
    <li> Enter password: password (siendo password la contraseña)</li>
    <li>Escribimos <b> select * from users; y se nos devolverá empty set 0.0 </b> </li>   
    <hr/>
    <li>Ahora escribimos en el navegador, localhost:5000/signup (esta es una de las rutas) </li>
    <li> Nos registramos (Introducimos nombre de usuario + password) </li>
    <hr/>
    <li>Escribimos <b> select * from users; y se nos devolverá el usuario con su id y la password hasheada </b> </li>   
</ul>
      
<hr/>

<b>Rutas de la aplicacion </b>
<ul>
<li>localhost:5000/</li>
<li>localhost:5000/signup  para registrarnos y que nos aparezca info en la base de datos</li>
<li>localhost:5000/login  accedemos con nuestro usuario y contraseña (<b>Nos tenemos que haber registrado previamente</b>) </li>
<li>localhost:5000/home nos devolverá la cadena  'You are <nombre de usuario>'</li>
 <li>localhost:5000/logout cerramos la sesion</li>
</ul>
