
#include <queue>


class Solution {
public:
    int maxDepth(TreeNode* root) {

        if(root == NULL)
            return 0;


        queue <TreeNode*> q;
        q.push(root);
        int depth = 0;

        while(q.size() > 0)
        {

            int n = q.size();

            while(n--)
            {

                TreeNode* curr = q.front();

                q.pop();

                if(curr->left != NULL)
                {
                    q.push(curr->left);
                }

                if(curr->right != NULL)
                {
                    q.push(curr->right);
                }
            }
            depth++;
        }
        return depth;
    }
};