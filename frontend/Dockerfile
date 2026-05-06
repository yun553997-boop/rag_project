# frontend/Dockerfile
# 第一阶段：编译打包
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm config set registry https://registry.npmmirror.com/ && npm install
COPY . .
RUN npm run build

# 第二阶段：Nginx 部署
FROM nginx:alpine
# 将第一阶段打包好的 dist 目录复制到 Nginx 下
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]