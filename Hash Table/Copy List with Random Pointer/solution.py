class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node_map = {}
        
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            node_map[current].next = node_map.get(current.next)
            node_map[current].random = node_map.get(current.random)
            current = current.next
            
        return node_map[head]