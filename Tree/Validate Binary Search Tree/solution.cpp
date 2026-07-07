/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool helper(TreeNode* root, TreeNode* min_val, TreeNode* max_val)
    {
        if(root == NULL)
        {
            return true;
        }

        if(min_val != NULL && root->val <= min_val->val)
        {
            return false;
        }

        if(max_val != NULL && root->val  >= max_val->val)
        {
            return false;
        }

        return helper(root->left, min_val, root) && helper(root->right, root, max_val);
    }

    bool isValidBST(TreeNode* root) {
        return helper(root, NULL, NULL);
    }
};