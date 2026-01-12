#!/usr/bin/python3

class Checkbook:
    """
    Une classe représentant un chéquier simple avec dépôt, retrait et consultation du solde.
    """

    def __init__(self):
        """
        Initialise un compte avec un solde de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant sur le compte.

        Paramètres:
            amount (float) : Le montant à déposer. Doit être >= 0.

        Effets :
            Augmente self.balance et affiche le dépôt et le solde actuel.
        """
        if amount < 0:
            print("Cannot deposit a negative amount.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du compte si le solde est suffisant.

        Paramètres:
            amount (float) : Le montant à retirer. Doit être >= 0.

        Effets :
            Diminue self.balance et affiche le retrait et le solde actuel.
            Affiche un message d'erreur si les fonds sont insuffisants.
        """
        if amount < 0:
            print("Cannot withdraw a negative amount.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du compte.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale du programme.
    Permet à l'utilisateur de déposer, retirer, consulter le solde, ou quitter.
    Gère les entrées invalides et empêche le plantage.
    """
    cb = Checkbook()
    
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            
            if action == 'exit':
                print("Exiting. Goodbye!")
                break
            elif action == 'deposit':
                amount_input = input("Enter the amount to deposit: $").strip()
                try:
                    amount = float(amount_input)
                    cb.deposit(amount)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            elif action == 'withdraw':
                amount_input = input("Enter the amount to withdraw: $").strip()
                try:
                    amount = float(amount_input)
                    cb.withdraw(amount)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
        
        # Gestion d'interruption clavier (Ctrl+C)
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break

        # Gestion d'un EOF (Ctrl+D)
        except EOFError:
            print("\nEnd of input. Exiting.")
            break


if __name__ == "__main__":
    main()
