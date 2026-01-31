        if self.root is None:
            print("(empty tree)")
            return

        lines, *_ = self._buildDiagram(self.root)
        for line in lines:
            print(line)