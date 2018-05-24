namespace PCMApp
{
    partial class MainWindow
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
			this.panelTop = new System.Windows.Forms.Panel();
			this.tableLayoutPanelMain = new System.Windows.Forms.TableLayoutPanel();
			this.treeViewCourse = new System.Windows.Forms.TreeView();
			this.tableLayoutPanelData = new System.Windows.Forms.TableLayoutPanel();
			this.tableLayoutPanelMessages = new System.Windows.Forms.TableLayoutPanel();
			this.tableLayoutPanelTopicMessage = new System.Windows.Forms.TableLayoutPanel();
			this.labelContentName = new System.Windows.Forms.Label();
			this.labelContent = new System.Windows.Forms.Label();
			this.tableLayoutPanelMessageEditor = new System.Windows.Forms.TableLayoutPanel();
			this.flowLayoutPanelRating = new System.Windows.Forms.FlowLayoutPanel();
			this.labelRating = new System.Windows.Forms.Label();
			this.trackBarRating = new System.Windows.Forms.TrackBar();
			this.labelRatingComment = new System.Windows.Forms.Label();
			this.textBox1 = new System.Windows.Forms.TextBox();
			this.tableLayoutPanelMain.SuspendLayout();
			this.tableLayoutPanelData.SuspendLayout();
			this.tableLayoutPanelMessages.SuspendLayout();
			this.tableLayoutPanelTopicMessage.SuspendLayout();
			this.tableLayoutPanelMessageEditor.SuspendLayout();
			this.flowLayoutPanelRating.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarRating)).BeginInit();
			this.SuspendLayout();
			// 
			// panelTop
			// 
			this.panelTop.Dock = System.Windows.Forms.DockStyle.Top;
			this.panelTop.Location = new System.Drawing.Point(0, 0);
			this.panelTop.Name = "panelTop";
			this.panelTop.Size = new System.Drawing.Size(912, 35);
			this.panelTop.TabIndex = 0;
			// 
			// tableLayoutPanelMain
			// 
			this.tableLayoutPanelMain.ColumnCount = 2;
			this.tableLayoutPanelMain.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 20.4947F));
			this.tableLayoutPanelMain.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 79.5053F));
			this.tableLayoutPanelMain.Controls.Add(this.treeViewCourse, 0, 0);
			this.tableLayoutPanelMain.Controls.Add(this.tableLayoutPanelData, 1, 0);
			this.tableLayoutPanelMain.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tableLayoutPanelMain.Location = new System.Drawing.Point(0, 35);
			this.tableLayoutPanelMain.Name = "tableLayoutPanelMain";
			this.tableLayoutPanelMain.RowCount = 1;
			this.tableLayoutPanelMain.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelMain.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
			this.tableLayoutPanelMain.Size = new System.Drawing.Size(912, 398);
			this.tableLayoutPanelMain.TabIndex = 1;
			// 
			// treeViewCourse
			// 
			this.treeViewCourse.Dock = System.Windows.Forms.DockStyle.Fill;
			this.treeViewCourse.Location = new System.Drawing.Point(3, 3);
			this.treeViewCourse.Name = "treeViewCourse";
			this.treeViewCourse.Size = new System.Drawing.Size(180, 392);
			this.treeViewCourse.TabIndex = 1;
			// 
			// tableLayoutPanelData
			// 
			this.tableLayoutPanelData.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Inset;
			this.tableLayoutPanelData.ColumnCount = 1;
			this.tableLayoutPanelData.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelData.Controls.Add(this.tableLayoutPanelMessageEditor, 0, 1);
			this.tableLayoutPanelData.Controls.Add(this.tableLayoutPanelMessages, 0, 0);
			this.tableLayoutPanelData.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tableLayoutPanelData.Location = new System.Drawing.Point(189, 3);
			this.tableLayoutPanelData.Name = "tableLayoutPanelData";
			this.tableLayoutPanelData.RowCount = 2;
			this.tableLayoutPanelData.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelData.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelData.Size = new System.Drawing.Size(720, 392);
			this.tableLayoutPanelData.TabIndex = 2;
			// 
			// tableLayoutPanelMessages
			// 
			this.tableLayoutPanelMessages.ColumnCount = 1;
			this.tableLayoutPanelMessages.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelMessages.Controls.Add(this.tableLayoutPanelTopicMessage, 0, 0);
			this.tableLayoutPanelMessages.Dock = System.Windows.Forms.DockStyle.Top;
			this.tableLayoutPanelMessages.Location = new System.Drawing.Point(5, 5);
			this.tableLayoutPanelMessages.Name = "tableLayoutPanelMessages";
			this.tableLayoutPanelMessages.RowCount = 2;
			this.tableLayoutPanelMessages.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 56.68449F));
			this.tableLayoutPanelMessages.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 43.31551F));
			this.tableLayoutPanelMessages.Size = new System.Drawing.Size(710, 151);
			this.tableLayoutPanelMessages.TabIndex = 2;
			// 
			// tableLayoutPanelTopicMessage
			// 
			this.tableLayoutPanelTopicMessage.ColumnCount = 1;
			this.tableLayoutPanelTopicMessage.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelTopicMessage.Controls.Add(this.labelContentName, 0, 0);
			this.tableLayoutPanelTopicMessage.Controls.Add(this.labelContent, 0, 1);
			this.tableLayoutPanelTopicMessage.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tableLayoutPanelTopicMessage.Location = new System.Drawing.Point(3, 3);
			this.tableLayoutPanelTopicMessage.Name = "tableLayoutPanelTopicMessage";
			this.tableLayoutPanelTopicMessage.RowCount = 3;
			this.tableLayoutPanelTopicMessage.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelTopicMessage.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelTopicMessage.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 20F));
			this.tableLayoutPanelTopicMessage.Size = new System.Drawing.Size(704, 79);
			this.tableLayoutPanelTopicMessage.TabIndex = 4;
			// 
			// labelContentName
			// 
			this.labelContentName.AutoSize = true;
			this.labelContentName.Dock = System.Windows.Forms.DockStyle.Left;
			this.labelContentName.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.labelContentName.Location = new System.Drawing.Point(3, 0);
			this.labelContentName.Name = "labelContentName";
			this.labelContentName.Size = new System.Drawing.Size(97, 29);
			this.labelContentName.TabIndex = 0;
			this.labelContentName.Text = "Задание";
			// 
			// labelContent
			// 
			this.labelContent.AutoSize = true;
			this.labelContent.Dock = System.Windows.Forms.DockStyle.Left;
			this.labelContent.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
			this.labelContent.Location = new System.Drawing.Point(3, 29);
			this.labelContent.Name = "labelContent";
			this.labelContent.Size = new System.Drawing.Size(91, 29);
			this.labelContent.TabIndex = 2;
			this.labelContent.Text = "Текст задания";
			// 
			// tableLayoutPanelMessageEditor
			// 
			this.tableLayoutPanelMessageEditor.ColumnCount = 1;
			this.tableLayoutPanelMessageEditor.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelMessageEditor.Controls.Add(this.flowLayoutPanelRating, 0, 0);
			this.tableLayoutPanelMessageEditor.Controls.Add(this.textBox1, 0, 1);
			this.tableLayoutPanelMessageEditor.Dock = System.Windows.Forms.DockStyle.Fill;
			this.tableLayoutPanelMessageEditor.Location = new System.Drawing.Point(5, 200);
			this.tableLayoutPanelMessageEditor.Name = "tableLayoutPanelMessageEditor";
			this.tableLayoutPanelMessageEditor.RowCount = 2;
			this.tableLayoutPanelMessageEditor.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
			this.tableLayoutPanelMessageEditor.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 129F));
			this.tableLayoutPanelMessageEditor.Size = new System.Drawing.Size(710, 187);
			this.tableLayoutPanelMessageEditor.TabIndex = 5;
			// 
			// flowLayoutPanelRating
			// 
			this.flowLayoutPanelRating.Controls.Add(this.labelRating);
			this.flowLayoutPanelRating.Controls.Add(this.trackBarRating);
			this.flowLayoutPanelRating.Controls.Add(this.labelRatingComment);
			this.flowLayoutPanelRating.Dock = System.Windows.Forms.DockStyle.Fill;
			this.flowLayoutPanelRating.Location = new System.Drawing.Point(3, 3);
			this.flowLayoutPanelRating.Name = "flowLayoutPanelRating";
			this.flowLayoutPanelRating.Size = new System.Drawing.Size(704, 52);
			this.flowLayoutPanelRating.TabIndex = 4;
			// 
			// labelRating
			// 
			this.labelRating.AutoSize = true;
			this.labelRating.Location = new System.Drawing.Point(3, 10);
			this.labelRating.Margin = new System.Windows.Forms.Padding(3, 10, 3, 0);
			this.labelRating.Name = "labelRating";
			this.labelRating.Size = new System.Drawing.Size(108, 13);
			this.labelRating.TabIndex = 1;
			this.labelRating.Text = "Оценка за задание:";
			// 
			// trackBarRating
			// 
			this.trackBarRating.Location = new System.Drawing.Point(117, 3);
			this.trackBarRating.Name = "trackBarRating";
			this.trackBarRating.Size = new System.Drawing.Size(202, 45);
			this.trackBarRating.TabIndex = 0;
			// 
			// labelRatingComment
			// 
			this.labelRatingComment.AutoSize = true;
			this.labelRatingComment.Location = new System.Drawing.Point(325, 10);
			this.labelRatingComment.Margin = new System.Windows.Forms.Padding(3, 10, 3, 0);
			this.labelRatingComment.Name = "labelRatingComment";
			this.labelRatingComment.Size = new System.Drawing.Size(125, 13);
			this.labelRatingComment.TabIndex = 2;
			this.labelRatingComment.Text = "Комментарий к оценке";
			// 
			// textBox1
			// 
			this.textBox1.Dock = System.Windows.Forms.DockStyle.Left;
			this.textBox1.Location = new System.Drawing.Point(3, 61);
			this.textBox1.Name = "textBox1";
			this.textBox1.Size = new System.Drawing.Size(242, 20);
			this.textBox1.TabIndex = 5;
			// 
			// MainWindow
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(912, 433);
			this.Controls.Add(this.tableLayoutPanelMain);
			this.Controls.Add(this.panelTop);
			this.Name = "MainWindow";
			this.Text = "PCM Application";
			this.tableLayoutPanelMain.ResumeLayout(false);
			this.tableLayoutPanelData.ResumeLayout(false);
			this.tableLayoutPanelMessages.ResumeLayout(false);
			this.tableLayoutPanelTopicMessage.ResumeLayout(false);
			this.tableLayoutPanelTopicMessage.PerformLayout();
			this.tableLayoutPanelMessageEditor.ResumeLayout(false);
			this.tableLayoutPanelMessageEditor.PerformLayout();
			this.flowLayoutPanelRating.ResumeLayout(false);
			this.flowLayoutPanelRating.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.trackBarRating)).EndInit();
			this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panelTop;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanelMain;
        private System.Windows.Forms.TreeView treeViewCourse;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanelData;
		private System.Windows.Forms.TableLayoutPanel tableLayoutPanelMessageEditor;
		private System.Windows.Forms.FlowLayoutPanel flowLayoutPanelRating;
		private System.Windows.Forms.Label labelRating;
		private System.Windows.Forms.TrackBar trackBarRating;
		private System.Windows.Forms.Label labelRatingComment;
		private System.Windows.Forms.TableLayoutPanel tableLayoutPanelMessages;
		private System.Windows.Forms.TableLayoutPanel tableLayoutPanelTopicMessage;
		private System.Windows.Forms.Label labelContentName;
		private System.Windows.Forms.Label labelContent;
		private System.Windows.Forms.TextBox textBox1;
	}
}

