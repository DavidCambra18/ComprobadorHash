/*
 * Autor: DavidCambra18 (https://github.com/DavidCambra18)
 * Descripción: Comprobador de hash para verificar si los hashes de los archivos
 * son iguales.
 * Repositorio: https://github.com/DavidCambra18/ComprobadorHash
 */

import java.util.Scanner;

public class comprobador_hash {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.println("Introduce el hash original del archivo: ");
		String original = sc.nextLine();

		System.out.println("Introduce el hash original del archivo: ");
		String comprobante = sc.nextLine();

		if (original.equalsIgnoreCase(comprobante))
			System.out.println("El hash original es igual al del archivo!");
		else
			System.out.println("El hash original NO es igual al del archivo :(");

		sc.close();
	}
}