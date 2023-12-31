#!"D:\xampp\perl\bin\perl.exe"
use strict;
use CGI;

my $cgi = new CGI;
my $numero1 = $cgi->param('numero1');
my $numero2 = $cgi->param('numero2');
my $operacion = $cgi->param('operacion');
my $resultado;

if ($numero1 !~ /^[0-9]+$/ or $numero2 !~ /^[0-9]+$/) {
    print $cgi->header("text/html");
    print 'Solo se aceptan números';
} else {
    print $cgi->header("text/html");

    if ($operacion eq 'sumar') {
        $resultado = $numero1 + $numero2;
        print 'El resultado de la suma es: ' . $resultado;
    } elsif ($operacion eq 'restar') {
        $resultado = $numero1 - $numero2;
        print 'El resultado de la resta es: ' . $resultado;
    } elsif ($operacion eq 'multiplicar') {
        $resultado = $numero1 * $numero2;
        print 'El resultado de la multiplicacion es: ' . $resultado;
    } elsif ($operacion eq 'dividir') {
        if ($numero2 != 0) {
            $resultado = $numero1 / $numero2;
            print 'El resultado de la division es: ' . $resultado;
        } else {
            print 'No es posible dividir por cero.';
        }
    } else {
        print 'Operación no válida.';
    }
}