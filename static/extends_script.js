function delete_thesis(url){
    is_delete = confirm('是否删除选题！');
    if (is_delete){
        window.open(url, '_self');
    }
}

function cancelTeacher(url, teacher_name){
    is_concel = confirm('是否取消选择' + teacher_name + '教师，取消选择后你的论文选题将同时被取消选择');
    if (is_concel){
        window.open(url, '_self');
    }
}

function upload_file(){
    var files = document.getElementById('uploadFile');
    var uploadFile = files.files[0];
    if (uploadFile){
        file_size = uploadFile.size; // 获取文件的大小
        if (file_size > 50*1024*1024){
            alert('上传文件不能超过50M！');
            files.outerHTML = files.outerHTML;  //情况file_input的内容
        }
    }else{
        alert('请添加文件！')
    }
}

/* 显示和隐藏不同意申请理由的输入框 */
$(document).ready(function() {
    $("#show_div").click(function() {
        $("#disggreReson").toggle();
    });
});

