#include "defines.h"
#include "actors.cpp"
#include "attacks.cpp"

#include <unistd.h>

int main()
{
	weaponInit();
	armorInit();
	string name;
	int job;
	cout << "Enter character name." << endl;
	cin >> name;
	cout << "Enter job.\n1. Warrior\n2. Mage\n3. Rogue\n" ;
	cin >> job;
	while (job > 3 || job < 1) //Job macros in defines.h
	{
		cout << "Enter a valid job\n";
		cin >> job;
	}
	Player player1(name, job);
	Goblin enemy;
	cout << "Player deals " << basicAttack(&player1, &enemy) << " damage!" << endl;
	cout << "Enemy deals " << basicAttack(&enemy, &player1) << " damage!" << endl;

	return 0;
}