# 使用 API 文档

本指南涵盖了使用现代工具进行 API 文档编写的最佳实践。

## RESTful APIs

在记录 REST APIs 时，包括：

- 端点URL：`https://api.example.com/v1/users`
- HTTP 方法：GET、POST、PUT、DELETE
- 请求/响应示例
- 身份验证要求

## GraphQL APIs

GraphQL 提供了一个具有灵活查询的单一端点：

```graphql
query GetUser($id: ID!) {
  user(id: $id) {
    name
    email
    posts {
      title
      content
    }
  }
}
```

## 工具

流行的文档工具包括：

- **Swagger/OpenAPI**：行业标准
- **Postman**：测试和文档
- **GitBook**：美观的文档平台
- **Claude**：AI 驱动的协助

访问 https://swagger.io 获取更多信息。