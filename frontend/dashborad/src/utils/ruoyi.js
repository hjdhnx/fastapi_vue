/**
 * 通用js方法封装处理
 * Copyright (c) 2019 ruoyi
 */
import axios from 'axios'
import { Notification, MessageBox, Message, Loading } from 'element-ui'
import fileDownload from 'js-file-download'
import { getToken } from '@/utils/auth'
import request from "@/utils/request";
let downloadLoadingInstance;
const baseURL = process.env.VUE_APP_BASE_API

// 日期格式化
export function parseTime(time, pattern) {
  if (arguments.length === 0 || !time) {
    return null
  }
  const format = pattern || '{y}-{m}-{d} {h}:{i}:{s}'
  let date
  if (typeof time === 'object') {
    date = time
  } else {
    if ((typeof time === 'string') && (/^[0-9]+$/.test(time))) {
      time = parseInt(time)
    } else if (typeof time === 'string') {
      time = time.replace(new RegExp(/-/gm), '/')
    }
    if ((typeof time === 'number') && (time.toString().length === 10)) {
      time = time * 1000
    }
    date = new Date(time)
  }
  const formatObj = {
    y: date.getFullYear(),
    m: date.getMonth() + 1,
    d: date.getDate(),
    h: date.getHours(),
    i: date.getMinutes(),
    s: date.getSeconds(),
    a: date.getDay()
  }
  const time_str = format.replace(/{(y|m|d|h|i|s|a)+}/g, (result, key) => {
    let value = formatObj[key]
    // Note: getDay() returns 0 on Sunday
    if (key === 'a') {
      return ['日', '一', '二', '三', '四', '五', '六'][value]
    }
    if (result.length > 0 && value < 10) {
      value = '0' + value
    }
    return value || 0
  })
  return time_str
}

// 表单重置
export function resetForm(refName) {
  if (this.$refs[refName]) {
    this.$refs[refName].resetFields()
  }
}

// 添加日期范围
export function addDateRange(params, dateRange) {
  var search = params
  search.begin_time = ''
  search.end_time = ''
  if (dateRange !== null && dateRange !== '') {
    search.begin_time = this.dateRange[0]
    search.end_time = this.dateRange[1]
  }
  return search
}

// 回显数据字典
export function selectDictLabel(datas, value) {
  var actions = []
  Object.keys(datas).map((key) => {
    if (datas[key].value === value) {
      actions.push(datas[key].label)
      return false
    }
  })
  return actions.join('')
}

// 通用下载方法
export function download(fileName, query = null,filename = null) {
  var download_url = '/report/excel_generate/' + fileName
  downloadLoadingInstance = Loading.service({ text: "正在下载数据，请稍候", spinner: "el-icon-loading", background: "rgba(0, 0, 0, 0.7)", })
  return request({
    url: download_url,
    method: 'get',
    responseType: 'arraybuffer',
    params: query
  }).then((response) => {
    let file_name = response.headers['content-disposition'].split('filename=')[1].split(';')[0]
    file_name = decodeURIComponent(escape(file_name))
    console.log(file_name)
    fileDownload(response.data, filename||file_name) // 如果用方法一 ，这里需要安装 npm install js-file-download --save ,然后引用
    downloadLoadingInstance.close();
  })
}

// 字符串格式化(%s )
export function sprintf(str) {
  var args = arguments
  var flag = true
  var i = 1
  str = str.replace(/%s/g, function() {
    var arg = args[i++]
    if (typeof arg === 'undefined') {
      flag = false
      return ''
    }
    return arg
  })
  return flag ? str : ''
}

// 转换字符串，undefined,null等转化为""
export function praseStrEmpty(str) {
  if (!str || str === 'undefined' || str === 'null') {
    return ''
  }
  return str
}

/**
 * 构造树型结构数据
 * @param {*} data 数据源
 * @param {*} id id字段 默认 'id'
 * @param {*} parent_id 父节点字段 默认 'parent_id'
 * @param {*} children 孩子节点字段 默认 'children'
 * @param {*} rootId 根Id 默认 0
 */
export function handleTree(data, id, parent_id, children, rootId) {
  id = id || 'id'
  parent_id = parent_id || 'parent_id'
  children = children || 'children'
  rootId = rootId || Math.min.apply(Math, data.map(item => { return item[parent_id]; })) || 0;
  // 对源数据深度克隆
  const cloneData = JSON.parse(JSON.stringify(data))
  // 循环所有项
  const treeData = cloneData.filter(father => {
    const branchArr = cloneData.filter(child => {
      // 返回每一项的子级数组
      return father[id] === child[parent_id]
    })
    branchArr.length > 0 ? father.children = branchArr : ''
    // 返回第一层
    return father[parent_id] === rootId || !father[parent_id]
  })
  return treeData !== '' ? treeData : data
}

// 验证是否为blob格式
export function blobValidate(data) {
  return data.type !== 'application/json'
}
