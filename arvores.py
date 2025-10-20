import sys

class NodeAVL:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def insert(self, key):
        self.root = self._insert(self.root, key)
        if self.root:
            print(f"Elemento {key} inserido na AVL.")
        else:
            print(f"Falha ao inserir {key} na AVL.")


    def _insert(self, root, key):
        if not root:
            return NodeAVL(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)
        if self.root is not None:
             print(f"Elemento {key} removido da AVL.")
        elif self.root is None and key == self.root.key:
             print(f"Elemento {key} removido da AVL. A árvore está vazia.")
        else:
            print(f"Elemento {key} não encontrado na AVL.")

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def search(self, key):
        result = self._search(self.root, key)
        if result:
            print(f"Elemento {key} encontrado na AVL.")
        else:
            print(f"Elemento {key} NÃO encontrado na AVL.")
        return result

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        
        if key < root.key:
            return self._search(root.left, key)
        
        return self._search(root.right, key)

    def print_tree(self):
        print("--- Árvore AVL (Impressão Pré-Ordem) ---")
        self._preOrder(self.root)
        print("\n----------------------------------------")

    def _preOrder(self, root):
        if not root:
            return
        
        print(f"{root.key} (H:{root.height}, B:{self.getBalance(root)})", end=" | ")
        self._preOrder(root.left)
        self._preOrder(root.right)

class NodeRBT:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1 

class RedBlackTree:
    def __init__(self):
        self.TNULL = NodeRBT(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def _search(self, node, key):
        if node == self.TNULL or key == node.key:
            return node
        
        if key < node.key:
            return self._search(node.left, key)
        
        return self._search(node.right, key)

    def _delete_fixup(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    s = x.parent.right
                
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rightRotate(s)
                        s = x.parent.right
                    
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    s = x.parent.left
                
                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.leftRotate(s)
                        s = x.parent.left
                    
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 0

    def _rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _insert_fixup(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def _preOrder(self, node):
        if node != self.TNULL:
            color = "Vermelho" if node.color == 1 else "Preto"
            print(f"{node.key} ({color})", end=" | ")
            self._preOrder(node.left)
            self._preOrder(node.right)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = NodeRBT(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1
        
        y = None
        x = self.root
        
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        
        if node.parent == None:
            node.color = 0
            print(f"Elemento {key} inserido na Rubro-Negra.")
            return
        
        if node.parent.parent == None:
            print(f"Elemento {key} inserido na Rubro-Negra.")
            return
        
        self._insert_fixup(node)
        print(f"Elemento {key} inserido na Rubro-Negra.")

    def delete(self, key):
        z = self.TNULL
        node = self.root
        
        while node != self.TNULL:
            if node.key == key:
                z = node
                break
            if node.key < key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print(f"Elemento {key} NÃO encontrado na Rubro-Negra.")
            return
        
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self.getMinValueNode(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == 0:
            self._delete_fixup(x)
        
        print(f"Elemento {key} removido da Rubro-Negra.")

    def search(self, key):
        result = self._search(self.root, key)
        if result != self.TNULL:
            print(f"Elemento {key} encontrado na Rubro-Negra.")
        else:
            print(f"Elemento {key} NÃO encontrado na Rubro-Negra.")
        return result

    def getMinValueNode(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def print_tree(self):
        print("--- Árvore Rubro-Negra (Impressão Pré-Ordem) ---")
        self._preOrder(self.root)
        print("\n------------------------------------------------")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def tree_operations_menu(tree):
    while True:
        print("\n--- Operações ---")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Buscar elemento")
        print("4. Imprimir árvore")
        print("5. Voltar ao menu principal")
        
        choice = input("Escolha uma operação: ")
        
        if choice == '1':
            key = get_int_input("Digite o valor para inserir: ")
            tree.insert(key)
        elif choice == '2':
            key = get_int_input("Digite o valor para remover: ")
            tree.delete(key)
        elif choice == '3':
            key = get_int_input("Digite o valor para buscar: ")
            tree.search(key)
        elif choice == '4':
            tree.print_tree()
        elif choice == '5':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main_menu():
    avl_tree = None
    rbt_tree = None
    
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("Qual tipo de árvore deseja criar/usar?")
        print("1. Árvore AVL")
        print("2. Árvore Rubro-Negra")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            if avl_tree is None:
                print("Criando uma nova Árvore AVL...")
                avl_tree = AVLTree()
            else:
                print("Usando a Árvore AVL existente.")
            tree_operations_menu(avl_tree)
            
        elif choice == '2':
            if rbt_tree is None:
                print("Criando uma nova Árvore Rubro-Negra...")
                rbt_tree = RedBlackTree()
            else:
                print("Usando a Árvore Rubro-Negra existente.")
            tree_operations_menu(rbt_tree)
            
        elif choice == '3':
            print("Encerrando o programa...")
            sys.exit()
            
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main_menu()