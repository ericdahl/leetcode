/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

static void traverse(struct TreeNode* root, int visited[], int* position) {
    if (!root) return;

    traverse(root->left, visited, position);
    visited[(*position)++] = root->val;
    traverse(root->right, visited, position);
}

static struct TreeNode* build_tree(struct TreeNode* tree, const int values[], const int left, const int right) {

    if (left >= right) return tree;

    const int length = right - left;
    const int l = left;
    const int m = l + length / 2;
    const int r = right;

    struct TreeNode* left_tree = build_tree(tree, values, l, m);
    struct TreeNode* right_tree = build_tree(tree, values, m + 1, r);

    struct TreeNode* n = calloc(1, sizeof(struct TreeNode));
    n->val = values[m];
    n->left = left_tree;
    n->right = right_tree;

    return n;
}


struct TreeNode* balanceBST(struct TreeNode* root) {
    // TODO: could save memory by pre-traversing to get size..
    // Linked list would slow down tree building..
    int visited[10000];
    int length = 0;
    traverse(root, visited, &length);

    return build_tree(NULL, visited, 0, length);
}