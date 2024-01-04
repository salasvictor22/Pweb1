#!"D:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;

my $nombreUniversidad     = $cgi->param('nombreUniversidad');
my $periodoLicenciamiento = $cgi->param('periodoLicenciamiento');
my $departamentoLocal     = $cgi->param('departamentoLocal');
my $denominacionPrograma  = $cgi->param('denominacionPrograma');

my $archivo_datos = 'ProgramasdeUniversidades.csv';

open my $fh, '<', $archivo_datos or die "No se pudo abrir el archivo $archivo_datos: $!";

<$fh>;
my @resultados;
while (<$fh>) {
    chomp;  
    my (
        $codigo_entidad, $nombre, $tipo_gestion, $estado_licenciamiento, $periodo_licenciamiento,
        $codigo_filial, $nombre_filial, $departamento_filial, $provincia_filial, $codigo_local,
        $departamento_local, $provincia_local, $distrito_local, $latitud_ubicacion, $longitud_ubicacion,
        $tipo_autorizacion_local, $denominacion_programa, $tipo_nivel_academico, $nivel_academico,
        $codigo_clase_programa_n2, $nombre_clase_programa_n2, $tipo_autorizacion_programa, $tipo_autorizacion_programa_local
    ) = split /,/, $_;

    if (
        ($nombreUniversidad eq '' || $nombre =~ /$nombreUniversidad/i) &&
        ($periodoLicenciamiento eq '' || $periodo_licenciamiento =~ /$periodoLicenciamiento/i) &&
        ($departamentoLocal eq '' || $departamento_local =~ /$departamentoLocal/i) &&
        ($denominacionPrograma eq '' || $denominacion_programa =~ /$denominacionPrograma/i)
    ) {
        push @resultados, {
            codigo_entidad            => $codigo_entidad,
            nombre                   => $nombre,
            tipo_gestion             => $tipo_gestion,
            estado_licenciamiento    => $estado_licenciamiento,
            periodo_licenciamiento   => $periodo_licenciamiento,
            codigo_filial            => $codigo_filial,
            nombre_filial            => $nombre_filial,
            departamento_filial      => $departamento_filial,
            provincia_filial         => $provincia_filial,
            codigo_local             => $codigo_local,
            departamento_local       => $departamento_local,
            provincia_local          => $provincia_local,
            distrito_local           => $distrito_local,
            latitud_ubicacion        => $latitud_ubicacion,
            longitud_ubicacion       => $longitud_ubicacion,
            tipo_autorizacion_local  => $tipo_autorizacion_local,
            denominacion_programa    => $denominacion_programa,
            tipo_nivel_academico     => $tipo_nivel_academico,
            nivel_academico          => $nivel_academico,
            codigo_clase_programa_n2 => $codigo_clase_programa_n2,
            nombre_clase_programa_n2 => $nombre_clase_programa_n2,
            tipo_autorizacion_programa            => $tipo_autorizacion_programa,
            tipo_autorizacion_programa_local      => $tipo_autorizacion_programa_local,
        };
    }
}

close $fh;

print $cgi->header('text/html');

print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultados de la Búsqueda</title>
    <link rel="stylesheet" type="text/css" href="estilos.css">
</head>
<body>

    <h1>Resultados de la Búsqueda</h1>

    <div class="resultados-container">
HTML

if (@resultados) {
    print <<HTML;
        <table border="1">
            <tr>
                <th>Código Entidad</th>
                <th>Nombre</th>
                <th>Tipo Gestión</th>
                <th>Estado Licenciamiento</th>
                <th>Periodo Licenciamiento</th>
                <th>Código Filial</th>
                <th>Nombre Filial</th>
                <th>Departamento Filial</th>s
                <th>Provincia Filial</th>
                <th>Código Local</th>
                <th>Departamento Local</th>
                <th>Provincia Local</th>
                <th>Distrito Local</th>
                <th>Latitud Ubicación</th>
                <th>Longitud Ubicación</th>
                <th>Tipo Autorización Local</th>
                <th>Denominación Programa</th>
                <th>Tipo Nivel Académico</th>
                <th>Nivel Académico</th>
                <th>Código Clase Programa N2</th>
                <th>Nombre Clase Programa N2</th>
                <th>Tipo Autorización Programa</th>
                <th>Tipo Autorización Programa Local</th>
            </tr>
HTML
    foreach my $resultado (@resultados) {
        print "<tr>";
        print "<td>$resultado->{codigo_entidad}</td>";
        print "<td>$resultado->{nombre}</td>";
        print "<td>$resultado->{tipo_gestion}</td>";
        print "<td>$resultado->{estado_licenciamiento}</td>";
        print "<td>$resultado->{periodo_licenciamiento}</td>";
        print "<td>$resultado->{codigo_filial}</td>";
        print "<td>$resultado->{nombre_filial}</td>";
        print "<td>$resultado->{departamento_filial}</td>";
        print "<td>$resultado->{provincia_filial}</td>";
        print "<td>$resultado->{codigo_local}</td>";
        print "<td>$resultado->{departamento_local}</td>";
        print "<td>$resultado->{provincia_local}</td>";
        print "<td>$resultado->{distrito_local}</td>";
        print "<td>$resultado->{latitud_ubicacion}</td>";
        print "<td>$resultado->{longitud_ubicacion}</td>";
        print "<td>$resultado->{tipo_autorizacion_local}</td>";
        print "<td>$resultado->{denominacion_programa}</td>";
        print "<td>$resultado->{tipo_nivel_academico}</td>";
        print "<td>$resultado->{nivel_academico}</td>";
        print "<td>$resultado->{codigo_clase_programa_n2}</td>";
        print "<td>$resultado->{nombre_clase_programa_n2}</td>";
        print "<td>$resultado->{tipo_autorizacion_programa}</td>";
        print "<td>$resultado->{tipo_autorizacion_programa_local}</td>";
        print "</tr>";
    }

    print <<HTML;
        </table>
HTML
} else {
    print "<p>No se encontraron resultados para la búsqueda.</p>";
}

print <<HTML;
    </div>

</body>
</html>
HTML